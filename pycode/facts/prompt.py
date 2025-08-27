"""
One-off example to query the stored facts using a RetrievalQA chain.

Prefer running `repl.py` for an interactive experience. This script now supports
printing references to matched facts when requested.

Usage:
  python prompt.py "Your question here"
  python prompt.py --refs "Your question here"  # always print sources
"""

import sys
from typing import List

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.schema import Document

from redundant_filter_retriever import RedundantFilterRetriever

from dotenv import load_dotenv
import langchain


def format_sources(docs: List[Document]) -> str:
    lines = []
    for i, d in enumerate(docs, 1):
        snippet = d.page_content.strip().replace("\n", " ")
        if len(snippet) > 180:
            snippet = snippet[:177] + "..."
        lines.append(f"[{i}] {snippet}")
    return "\n".join(lines)


def main() -> int:
    # Comment out the following to suppress the debug info
    langchain.debug = False
    load_dotenv()

    # Parse simple args
    args = [a for a in sys.argv[1:] if a.strip()]
    force_refs = False
    if args and args[0] == "--refs":
        force_refs = True
        args = args[1:]
    question = "Things about languages?" if not args else " ".join(args)

    chat = ChatOpenAI(temperature=0)
    embeddings = OpenAIEmbeddings()

    db = Chroma(persist_directory="emb", embedding_function=embeddings)
    retriever = RedundantFilterRetriever(embeddings=embeddings, chroma=db)

    chain = RetrievalQA.from_chain_type(
        llm=chat,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True,
    )

    # Heuristic: if the user asks for references/sources/citations, show them
    ql = question.lower()
    wants_refs = any(k in ql for k in ["reference", "references", "source", "sources", "cite", "citation", "citations"]) or force_refs

    result = chain({"query": question})
    answer = result.get("result", "").strip()
    print(answer)
    if wants_refs:
        docs = result.get("source_documents") or []
        if docs:
            print("\nSources:")
            print(format_sources(docs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

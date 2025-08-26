import os
import time
from pathlib import Path
from typing import List, Tuple, Optional

from dotenv import load_dotenv
import langchain

from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import Document

from redundant_filter_retriever import RedundantFilterRetriever

FACTS_PATH = Path("facts.txt")
EMB_DIR = "emb"


def read_facts_scope() -> Tuple[int, List[str]]:
    if not FACTS_PATH.exists():
        return 0, []
    text = FACTS_PATH.read_text(encoding="utf-8", errors="ignore").lower()
    lines = [ln for ln in text.splitlines() if ln.strip()]
    topics: List[str] = []
    buckets = {
        "Animals": [
            "ostrich",
            "elephant",
            "snail",
            "panda",
            "shark",
            "zebra",
            "penguin",
            "owl",
            "seahorse",
            "wombat",
            "dolphin",
        ],
        "Geography": [
            "continent",
            "country",
            "desert",
            "river",
            "mountain",
            "reef",
            "ocean",
            "falls",
            "kilimanjaro",
            "everest",
            "sahara",
            "nile",
            "antarctica",
            "australia",
            "canada",
        ],
        "Space": [
            "mars",
            "venus",
            "saturn",
            "moon",
            "solar",
            "olympus mons",
            "sunset",
            "atmosphere",
            "universe",
        ],
        "History": [
            "ancient",
            "greek",
            "olympic",
            "world cup",
            "einstein",
            "marie curie",
            "charlie chaplin",
            "ray tomlinson",
            "queen elizabeth",
            "martin luther king",
        ],
        "Language": ["english", "word", "language", "japanese", "ok"],
        "Science": [
            "atom",
            "bacteria",
            "physics",
            "chemistry",
            "cartilage",
            "density",
            "regenerate",
            "mpemba",
            "cells",
            "blood",
        ],
    }
    for name, keys in buckets.items():
        if any(k in text for k in keys):
            topics.append(name)
    return len(lines), topics


def print_scope_banner(db_ready: bool, strict: bool = False, k: int = 4, threshold: float = 0.25) -> None:
    count, topics = read_facts_scope()
    print("=" * 70)
    print("Facts REPL")
    if FACTS_PATH.exists():
        mtime = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime(FACTS_PATH.stat().st_mtime)
        )
        print(f"- facts file: {FACTS_PATH.resolve()}")
        print(f"- facts count: ~{count} lines")
        print(f"- last updated: {mtime}")
        if topics:
            print(f"- topics include: {', '.join(sorted(topics))}")
    else:
        print("- facts file: MISSING (expected facts.txt in this folder)")
    print(f"- vector store: {'ready' if db_ready else 'not found'} (dir: {EMB_DIR}/)")
    mode = "STRICT" if strict else "DEFAULT"
    print(f"- mode: {mode}  (k={k}, threshold={threshold:.2f})")
    print(
        "- try: Which continent is least populated?  or  Tell me 2 facts about Mars"
    )
    print("- commands: :help  :scope  :sources  :rebuild  :clear  :exit")
    print("=" * 70)


def ensure_db(embeddings: OpenAIEmbeddings, allow_build: bool = True) -> Optional[Chroma]:
    emb_path = Path(EMB_DIR)
    if emb_path.exists() and any(emb_path.iterdir()):
        return Chroma(persist_directory=EMB_DIR, embedding_function=embeddings)
    if not allow_build:
        return None
    print("No vector index found in 'emb/'. Build it from facts.txt now? [y/N] ", end="", flush=True)
    choice = input().strip().lower()
    if choice != "y":
        return None
    if not FACTS_PATH.exists():
        print("facts.txt not found. Please add it and try again.")
        return None
    if not os.getenv("OPENAI_API_KEY"):
        print("OPENAI_API_KEY is missing. Add it to .env or environment and retry.")
        return None
    print("Building index (this uses your OpenAI API and may incur cost)...")
    splitter = CharacterTextSplitter(separator="\n", chunk_size=200, chunk_overlap=0)
    docs = TextLoader(str(FACTS_PATH)).load_and_split(text_splitter=splitter)
    db = Chroma.from_documents(docs, embedding=embeddings, persist_directory=EMB_DIR)
    print("Index built and saved to emb/")
    return db


def format_sources(docs: List[Document]) -> str:
    lines = []
    for i, d in enumerate(docs, 1):
        snippet = d.page_content.strip().replace("\n", " ")
        if len(snippet) > 180:
            snippet = snippet[:177] + "..."
        lines.append(f"[{i}] {snippet}")
    return "\n".join(lines)


def main() -> None:
    load_dotenv()
    langchain.debug = False  # default off; toggleable if needed

    embeddings = OpenAIEmbeddings()
    db = ensure_db(embeddings, allow_build=True)
    chat = ChatOpenAI(temperature=0)

    if db is None:
        # allow REPL; users can :rebuild later
        print_scope_banner(db_ready=False)
    else:
        print_scope_banner(db_ready=True)

    show_sources = False
    strict_mode = False
    top_k = 4
    score_threshold = 0.25

    strict_prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=(
            "You are a cautious facts assistant.\n"
            "Use ONLY the information in the CONTEXT to answer the QUESTION.\n"
            "If the answer is not clearly contained in the context, respond exactly with:\n"
            "Out of scope: I don't have that information in my facts.\n\n"
            "CONTEXT:\n{context}\n\nQUESTION: {question}\nANSWER:"
        ),
    )

    current_retriever = None

    def build_chain(current_db: Optional[Chroma]):
        nonlocal current_retriever
        if current_db is None:
            current_retriever = None
            return None
        if strict_mode:
            # Built-in retriever with similarity score threshold
            current_retriever = current_db.as_retriever(
                search_type="similarity_score_threshold",
                search_kwargs={"score_threshold": score_threshold, "k": top_k},
            )
        else:
            current_retriever = RedundantFilterRetriever(
                embeddings=embeddings, chroma=current_db, k=top_k
            )
        return RetrievalQA.from_chain_type(
            llm=chat,
            retriever=current_retriever,
            chain_type="stuff",
            return_source_documents=True,
            chain_type_kwargs={"prompt": strict_prompt} if strict_mode else None,
        )

    chain = build_chain(db)

    while True:
        try:
            inp = input("facts> ").strip()
        except EOFError:
            print()
            break
        except KeyboardInterrupt:
            print()
            continue

        if not inp:
            continue
        if inp in (":q", ":quit", ":exit"):
            break
        if inp == ":help":
            print(":help, :scope, :sources, :rebuild, :strict, :topk <n>, :thresh <0-1>, :clear, :exit")
            continue
        if inp == ":scope":
            print_scope_banner(db_ready=db is not None, strict=strict_mode, k=top_k, threshold=score_threshold)
            continue
        if inp == ":clear":
            os.system("clear" if os.name != "nt" else "cls")
            continue
        if inp == ":sources":
            show_sources = not show_sources
            print(f"sources {'ON' if show_sources else 'OFF'}")
            continue
        if inp.startswith(":topk"):
            parts = inp.split()
            if len(parts) == 2 and parts[1].isdigit():
                top_k = max(1, min(10, int(parts[1])))
                print(f"k set to {top_k}")
                chain = build_chain(db)
            else:
                print("Usage: :topk <n>")
            continue
        if inp.startswith(":thresh"):
            parts = inp.split()
            try:
                if len(parts) == 2:
                    v = float(parts[1])
                    if 0.0 <= v <= 1.0:
                        score_threshold = v
                        print(f"threshold set to {score_threshold:.2f}")
                        chain = build_chain(db)
                    else:
                        print("Threshold must be between 0 and 1.")
                else:
                    print("Usage: :thresh <0-1>")
            except ValueError:
                print("Usage: :thresh <0-1>")
            continue
        if inp == ":strict":
            strict_mode = not strict_mode
            print(f"strict mode {'ON' if strict_mode else 'OFF'}")
            chain = build_chain(db)
            continue
        if inp == ":rebuild":
            db = ensure_db(embeddings, allow_build=True)
            chain = build_chain(db)
            continue

        if chain is None:
            print("No index available. Run :rebuild first.")
            continue

        try:
            # Pre-flight gate: if retriever returns no docs, abstain without calling LLM
            try:
                docs = current_retriever.get_relevant_documents(inp) if current_retriever else []
            except Exception:
                docs = []
            if not docs:
                print("Out of scope: I don't have that information in my facts.")
                continue

            result = chain({"query": inp})
        except KeyboardInterrupt:
            print("\nCancelled.")
            continue
        except Exception as e:
            print(f"Error: {e}")
            continue

        print(result.get("result", "").strip())
        if show_sources:
            docs = result.get("source_documents") or []
            if docs:
                print("\nSources:")
                print(format_sources(docs))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

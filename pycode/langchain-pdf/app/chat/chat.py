from app.chat.models import ChatArgs

# Line 1 and build_chat was initiated with the package
# The rest has been added retroactively
from app.chat.vector_stores.pinecone import build_retriever

# [FOLLOW UP: ADDENDUM: chat.py: ConversationalRetrievalChain]
# from langchain.chains import ConversationalRetrievalChain
# The above line is being commented out in favor of the 
# following, in order to enable streaming support to the
# ConversationalRetrievalChain and our application in turn.
# [REFERENCE: retrieval.py]
from app.chat.chains.retrieval import StreamingConversationalRetrievalChain

from app.chat.llms.chatopenai import build_llm
from app.chat.memories.sql_memory import build_memory

def build_chat(chat_args: ChatArgs):
    """
    :param chat_args: ChatArgs object containing
        conversation_id, pdf_id, metadata, and streaming flag.

    :return: A chain

    Example Usage:

        chain = build_chat(chat_args)
    """
    # The following retriever has been properly scoped.
    # See pinecone.py and __init__.py for details on
    # pdf_id used for scoping our custom retriever
    retriever = build_retriever(chat_args)
    llm = build_llm(chat_args)
    memory = build_memory(chat_args)

#    return ConversationalRetrievalChain.from_llm(
# The following is the result of [FOLLOW UP: ADDENDUM: chat.py: ConversationalRetrievalChain]
    return StreamingConversationalRetrievalChain.from_llm(
            llm=llm,
            memory=memory,
            retriever=retriever
            )

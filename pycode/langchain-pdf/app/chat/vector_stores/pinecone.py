import os
from pinecone import Pinecone, ServerlessSpec
from langchain.vectorstores import Pinecone as LangchainPinecone
from app.chat.embeddings.openai import embeddings

# Initializing the pinecone client
#pinecone.init(
#        api_key=os.getenv("PINECONE_API_KEY"),
#        environment=os.getenv("PINECONE_ENV_NAME")
#        )

# The following has been added after asking from the AI
# above has been deprecated
pc = Pinecone(
        api_key=os.getenv("PINECONE_API_KEY")
        )

# Langchain wrapper for pinecone
vector_store = LangchainPinecone.from_existing_index(
        os.getenv("PINECONE_INDEX_NAME"), 
        embeddings
        )

# Building our retriever. Ref: __init__.py 
def build_retriever(chat_args):
    search_kwargs = {
            "filter": {
                # The following to keep a particular
                # conversation scoped to one specific
                # uploaded PDF file which is distinguished
                # by a unique id assigned to it.
                "pdf_id": chat_args.pdf_id
                }}
    return vector_store.as_retriever(
            search_kwargs = search_kwargs
            )

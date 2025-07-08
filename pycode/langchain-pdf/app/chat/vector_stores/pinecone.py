import os
import pinecone
from langchain.vectorstores import Pinecone
from app.chat.embeddings.openai import embeddings

# Initializing the pinecone client
pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"),
        environment=os.getenv("PINECONE_ENV_NAME")
        )

# Langchain wrapper for pinecone
vector_store = Pinecone.from_existing_index(
        os.getenv("PINECONE_INDEX_NAME"), embeddings
        )



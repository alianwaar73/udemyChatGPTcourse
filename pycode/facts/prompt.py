# File to enable a user type in a query. Contains code for chains to do that

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

# In the following import we import RetrievalQA, a chain that contains system and human message chains within to make prompting and retrieving relavant information, in the context of an application such as this project, from documents smoother.
from langchain.chains import RetrievalQA

from langchain.chat_models import ChatOpenAI

# Removing document duplication stored in our ChromaDB (vector store) using the following import for our custom Retriever class that contains this functionality.
from redundant_filter_retriever import RedundantFilterRetriever

# Following is to load our OpenAI API key
from dotenv import load_dotenv
import langchain

# Comment out the following to suppress the debug info
langchain.debug = True

load_dotenv()

chat = ChatOpenAI()
embeddings = OpenAIEmbeddings()

# In the following a slightly different way to create a Chroma instance than done in main.py. The reason being here we merely want an access to it instead of always populating it with docs in order to decouple the functionalities of prompting and storing
db = Chroma(
        persist_directory="emb",
        # [ ] Slightly confused with the following line. Are we re        # calculating the embeddings here? If so then why? Shouldn        #  't we just be accessing it somehow?
        embedding_function=embeddings
        )

## Uncomment the following and comment out the block next to it to use default retriever
# retriever = db.as_retriever()
retriever = RedundantFilterRetriever(
        embeddings=embeddings,
        chroma=db
        )

chain = RetrievalQA.from_chain_type(
        llm=chat,
        retriever=retriever,
        chain_type="stuff"
        )

result = chain.run("Things about languages?")

print(result)

####################################
### Embeddings and chunking text ###
####################################

######################################################################################
### This is concept introducing file for text chunking, embeddings, and vector store #
### It has a problem where every time this file is run the same (embeddings) results #
### are calculated on each run and stored in a vector db. To solve this problem, the #
### processes of embedding calculation, storage in a vector db, and prompting are    #
### split in separate files with indicative names in the project directory.          #
######################################################################################
from langchain.document_loaders import TextLoader
from dotenv import load_dotenv

# Following is for text chunking
from langchain.text_splitter import CharacterTextSplitter

from langchain.embeddings import OpenAIEmbeddings

# Following is an import for an opensource vector store called chromadb for embedding management
from langchain.vectorstores.chroma import Chroma

# Loading the environment file that contains OpenAI's API key
load_dotenv()

# Generating embeddings
embeddings = OpenAIEmbeddings()

# Text chunking or splitting criterion follows below
text_splitter = CharacterTextSplitter(
        # Following is a delimitor or what to see when splitting a blob of text
        separator="\n",
        chunk_size=200, # Characters long
        # The following, when non-zero, becomes more meaningful in long documents such as pdfs to avoid awkward hardcore text splitting. The value of 0 is fine for a short .txt file containing a list of facts. Simply chunking the list right now.
        chunk_overlap=0
        )

loader = TextLoader("facts.txt")

# Following is a debug block to see how text_splitter is chunking our input document with the given settings
docs = loader.load_and_split(
        text_splitter=text_splitter
        )

#docs = loader.load()

# Creating the vector store for our embeddings
# The following also costs money. [ ] How much? An analysis could potentially be performed
db = Chroma.from_documents(
        docs,
        # A (mis-)convention to note here is the absence of an 's' in the following keyword of 'embedding' to which (conventionally) embeddings with an 's', as generated above, is assigned
        embedding=embeddings,
        # Calculated embeddings are stored within this directory which is created inside the main project directory
        persist_directory="emb"
        )

# Searing the above created embedding's db for a document based on an input. Uncomment the following and comment out the line next to it to also print out (embedding) similarity score
#results = db.similarity_search_with_score(
results = db.similarity_search(
        "Which is the most powerful passport in the world?",
        # The following specifies the number of chunks shown on the output. Uncomment to specify. Default is 4
        # k=1
        )

#for doc in docs:
#    print(doc.page_content)
#    print("\n")

for result in results:
    print("\n")
    # This tuple prints out the (embedding) similarity score given out search input. Uncomment to see for debugging
    # print(result[1])
    # This tuple prints out the actual content or the chunk related to our input search. Uncomment for debugging
    # print(result[0].page_content)
    print(result.page_content)

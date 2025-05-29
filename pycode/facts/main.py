### Embeddings and chunking text ###
from langchain.document_loaders import TextLoader
from dotenv import load_dotenv

# Following is for text chunking
from langchain.text_splitter import CharacterTextSplitter

# Loading the environment file that contains OpenAI's API key
load_dotenv()

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

for doc in docs:
    print(doc.page_content)
    print("\n")

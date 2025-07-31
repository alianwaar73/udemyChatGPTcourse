from functools import partial
from .pinecone import build_retriever

# The following is a dictionary to map retriever names
# to their respective retriever functions with specific 
# parameters.
retriever_map = {
    # Whereas, the k parameter indicates the NUMBER of
    # top results to return from the retriever.
    "pinecone_1" : partial(build_retriever, k=1),
    "pinecone_2" : partial(build_retriever, k=2),
    "pinecone_3" : partial(build_retriever, k=3)
}

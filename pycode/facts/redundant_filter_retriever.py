##################################################################
### Main purpose of this file is to modify the source code       #
### of RetrieverQA to include the functionality of removing      #
### duplicate stored documents using their embedding information.###################################################################

from langchain.embeddings.base import Embeddings
from langchain.vectorstores import Chroma
from langchain.schema import BaseRetriever
from typing import List

##################################################################
### IMPORTANT: This customa class RedundantFilterRetriever is used### inside the prompt.py file as an import ######################
#################################################################


# The following custom class extends the BaseRetriever class to 
# include the above mentioned functionality

class RedundantFilterRetriever(BaseRetriever):
    # Requires user to input what sort of method should be used to calculate embeddings. Such as OpenAI, as in this case
    # Same for chroma instance in order not to hardcode the persist directory
    embeddings: Embeddings
    chroma: Chroma
    k: int = 4

    def get_relevant_documents(self, query) -> List:
        # Calculate embeddings for the query string
        emb = self.embeddings.embed_query(query)

        # Feed the calculated embedding into MMR search with a configurable k
        return self.chroma.max_marginal_relevance_search_by_vector(
            embedding=emb,
            k=self.k,
            # In the following lambda ranges from 0 to 1; higher values allow more repetitiveness
            lambda_mult=0.8,
        )

# [ ] The following block of code is customary to include. For the purposes of this project the above block suffices.

async def aget_relevant_documents(self):
    return []

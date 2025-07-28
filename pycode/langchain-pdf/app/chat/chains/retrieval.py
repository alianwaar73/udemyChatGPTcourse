from langchain.chains import ConversationalRetrievalChain
from app.chat.chains.streamable import StreamableChain

# The following class simply adds streaming functionality
# to ConversationalRetrievalChain
# Approach: MIXIN
# [Reference:] Refer to the streamable.py file for details
# on enabling the streaming function for different chain types
# and why is it required.
# [ADDENDUM: chat.py: ConversationalRetrievalChain]
class StreamingConversationalRetrievalChain(StreamableChain, ConversationalRetrievalChain):
    pass

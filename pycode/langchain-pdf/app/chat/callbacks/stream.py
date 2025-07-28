from langchain.callbacks.base import BaseCallbackHandler

class StreamingHandler(BaseCallbackHandler):
    # [ADDENDUM FOLLOW UP:] The following __init__ function
    # is added to address the issue of users using a single
    # instance of Queue and StreamingHandler. 
    # The following modification, affects the queue.put
    # functions that follow. queue.put is changed to 
    # self.queue.put
    def __init__(self, queue):
        self.queue = queue

    # on_llm_new_token is a special function in
    # langchain's source code.
    def on_llm_new_token(self, token, **kwargs):
        # [DEBUG:] The following line can be uncommented
        # print(token)
        # The following is the intercept buffer-zone
        # values coming from OpenAI stream are put into
        # the queue that will be yielded on the langchain-
        # -side to enable streaming from it to us
        # queue.put(token)
        self.queue.put(token)
    
    # The following is to take care of our infinitely
    # running while loop below in langchain-side
    # In order to achieve this None is put in the queue
    # as a signal for while loop that the OpenAI response
    # has finished. [JUAI:] Discuss potential caveats of
    # using None. [ ] Any better alternatives?
    def on_llm_end(self, response, **kwargs):
        # queue.put(None)
        self.queue.put(None)

    # The following for the case if OpenAI-side response
    # fails or errors
    def on_llm_error(self, error, **kwargs):
        # queue.put(None)
        self.queue.put(None)



# This file is written to implement streaming feature in
# the application. Particularly, as per the lectures, llms
# by nature, readily stream but chains do not. That is why, a
# work-around is to create this test.py file.

# [IMPLEMENTING STREAMING:] In order to *handle* the 
# ChatOpenAI-langchain streaming
# part. The file implements a custom handler that interacts
# with the tokens (character chunks) coming from the 
# ChatOpenAI side.

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks.base import BaseCallbackHandler
from dotenv import load_dotenv

# [Chain-side streaming:] Importing python's built-in Queue 
# data structure to
# implement langchain-side streaming. Values placed inside
# the Queue will be yielded for streaming functionality
from queue import Queue

# The following import is to implement concurrency to 
# properly implement streaming on langchain-side 
from threading import Thread

load_dotenv()

queue = Queue()

# [JUAI:] in the README for the following block as well
# This particular step can be thought of as an intercepting
# step to capture the streaming bit on OpenAI->langchain
class StreamingHandler(BaseCallbackHandler):
    # on_llm_new_token is a special function in
    # langchain's source code.
    def on_llm_new_token(self, token, **kwargs):
        # [DEBUG:] The following line can be uncommented
        # print(token)
        # The following is the intercept buffer-zone
        # values coming from OpenAI stream are put into
        # the queue that will be yielded on the langchain-
        # -side to enable streaming from it to us
        queue.put(token)
    
    # The following is to take care of our infinitely
    # running while loop below in langchain-side
    # In order to achieve this None is put in the queue
    # as a signal for while loop that the OpenAI response
    # has finished. [JUAI:] Discuss potential caveats of
    # using None. [ ] Any better alternatives?
    def on_llm_end(self, response, **kwargs):
        queue.put(None)

    # The following for the case if OpenAI-side response
    # fails or errors
    def on_llm_error(self, error, **kwargs):
        queue.put(None)

# [IMPORTANT:] ChatOpenAI() can take an argument of 
# ChatOpenAI(streaming=True). This is the OpenAI-Langchain 
# part. Instead one bulk of text OpenAI sends chunks of 
# information as it generates a response. BUT from Langchain
# to us, we see no obserable difference in terms of streaming
# on or off. For this see below in [IMPORTANT: FOLLOW UP]
chat = ChatOpenAI(
    streaming=True,
    callbacks=[StreamingHandler()]
)

# The following is the chain-part as discussed in the primer
# of this file. Chains always like to output bulk text as
# output! They keep waiting, even if ChatOpenAI streams to
# them, until the response is complete.
prompt = ChatPromptTemplate.from_messages([
    ("human",
     "{content}"
    )
])

# Object-orientation takes place in the following.
# class: StreamingChain; subclass: LLMChain
class StreamingChain(LLMChain):
    def stream(self, input):
        # If used as is the self(input) part keeps waiting
        # until the queue on OpenAI is all filled up. That
        # the langchain-side limitation. It does not move
        # ahead to the while loop. So this way streaming
        # is an illusion.
        # [JUAI:] In order to solve this, concurrency is 
        # used bY making use of threads. It is not 
        # parallelism. [ ] README should address this.
        def task():
            self(input)

        Thread(target=task).start()
        # The following creates a generator that will be
        # iterated over to implement streaming. *yield*
        # is the keyword to do it. Such as:
        # yield 'hi'
        # yield 'there'
        # Reading the values from the queue populated above
        # with the stream coming from OpenAI side
        while True:
            token = queue.get()
            if token is None:
                break
            yield token

chain = StreamingChain(
    llm=chat,
    prompt=prompt
)

# The following was the native way. The above is post
# (intercept) handler implementation.
# chain = LLMChain(
#    llm=chat,
#    prompt=prompt
# )

# output = chain("Tell me a joke!")
# print(output)

# [JUAI:] Include some explanation on the following in the
# README
# One can try the following:
# for output in chain.stream(input={"content":"tell me a joke!"}):
#           print(output)
# Even the above will not stream as per the (being used)
# implementation of langchain! That is the chains not being
# okay with streaming. They always wait until the full
# response!

# messages = prompt.format_messages(
#    content="Tell a joke!"
# )

# [IMPORTANT: FOLLOW UP:] In python chat is an object can be
# treated as a function. chat.__call__(messages) and
# chat.invoke(messages) is the same. However, there is a
# third way, chat.stream(messages). Using this, we get 
# text streaming in from langchain to us path irrespective of
# the value of streaming flag set above in ChatOpenAI. My
# guess is, that part is dictated by the architecture of the 
# application itself!
# output = chat(messages)
# for message in chat.stream(messages):
#    print(message.content) # langchain-us streaming in action

for output in chain.stream(input={"content": "Tell a millenial joke"}):
    print(output)

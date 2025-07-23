# This file is written to implement streaming feature in
# the application. Particularly, as per the lectures, llms
# by nature, readily stream but chains do not. That is why, a
# work-around is to create this test.py file.

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

# [IMPORTANT:] ChatOpenAI() can take an argument of 
# ChatOpenAI(streaming=True). This is the OpenAI-Langchain 
# part. Instead one bulk of text OpenAI sends chunks of 
# information as it generates a response. BUT from Langchain
# to us, we see no obserable difference in terms of streaming
# on or off. For this see below in [IMPORTANT: FOLLOW UP]
chat = ChatOpenAI()

# The following is the chain-part as discussed in the primer
# of this file.
prompt = ChatPromptTemplate.from_messages([
    ("human",
     "{content}"
    )
])

chain = LLMChain(
    llm=chat,
    prompt=prompt
)

messages = prompt.format_messages(
    content="Tell a joke!"
)

# [IMPORTANT: FOLLOW UP:] In python chat is an object can be
# treated as a function. chat.__call__(messages) and
# chat.invoke(messages) is the same. However, there is a
# third way, chat.stream(messages). Using this, we get 
# text streaming in from langchain to us path irrespective of
# the value of streaming flag set above in ChatOpenAI. My
# guess is, that part is dictated by the architecture of the 
# application itself!
# output = chat(messages)
for message in chat.stream(messages):
    print(message.content) # langchain-us streaming in action

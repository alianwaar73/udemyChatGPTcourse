# HumanMessagePromptTemplate: For user input
# ChatPromptTemplate: ??

from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate

# import langchain.llms implies a completion model the following is different

from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

# Importing our API key from the environment variable
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI()

# Start of a chain
prompt = ChatPromptTemplate(
        input_variables=["content"],
        messages=[
            HumanMessagePromptTemplate.from_template("{content}")
            ]
        )

chain = LLMChain(
        llm=chat,
        prompt=prompt
        )

while True:
    content = input(">> ")

    result = chain({"content": content})

    print(result["text"])

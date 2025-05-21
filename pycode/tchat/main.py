# HumanMessagePromptTemplate: For user input
# ChatPromptTemplate: ??

from langchain.prompts import MessagesPlaceholder, HumanMessagePromptTemplate, ChatPromptTemplate

# import langchain.llms implies a completion model the following is different

from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

# Importing our API key from the environment variable
from dotenv import load_dotenv

# Incorporating memory into our application so that pervious messages and responses are saved and can be referred to and conversations can go on naturally. ConversationBufferMemory is to store history of an on going chat.
# Whereas FileChatMessageHistory is to store conversations between boots of the program or application!
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory

load_dotenv()

chat = ChatOpenAI()

memory = ConversationBufferMemory(
        # Whereas messages.json file acts as a DB that stores
        # old chats that can be referred to whenever the application is booted. The constructor FileChatMessageHistory automatically creates the file with the name provided to it as the input argument.
        chat_memory=FileChatMessageHistory("messages.json"),
        memory_key="messages", 
        return_messages=True
        )

# Start of a chain
prompt = ChatPromptTemplate(
        # The variable messages is so that previously stored messages can be referred to
        input_variables=["content", "messages"],
        messages=[
            # The following line is for the aspect of memory
            MessagesPlaceholder(variable_name="messages"),
            HumanMessagePromptTemplate.from_template("{content}")
            ]
        )

chain = LLMChain(
        llm=chat,
        prompt=prompt,
        # Wiring the memory in
        memory=memory
        )

while True:
    content = input(">> ")

    result = chain({"content": content})

    print(result["text"])

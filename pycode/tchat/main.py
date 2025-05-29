# HumanMessagePromptTemplate: For user input
# ChatPromptTemplate: ??

from langchain.prompts import MessagesPlaceholder, HumanMessagePromptTemplate, ChatPromptTemplate

# import langchain.llms implies a [ ] completion model the following is different(!?)

from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

# Importing our API key from the environment variable file
from dotenv import load_dotenv

### Incorporating memory into our application so that pervious messages and responses are saved and can be referred to and conversations can go on naturally. ConversationBufferMemory is to store history of an on going chat for a smoother and natural flow of conversation. ###
# Whereas FileChatMessageHistory is to store conversations between boots of the program or application! This is done by storing a session's interactions in a referenceable file such as messages.json in our case.
# from langchain.memory import ConversationBufferMemory, FileChatMessageHistory

### IMPORTANT ### The above line is commented out to replace ConversationBufferMemory with ConversationSummaryMemory which is more cost effective as it uses its own chain with a language model provided within to summarise all the previous conversations when generating a new response. BUT ConversationSummaryMemory does not seem to remember between app bootups! As there is no saved file such as messages.json that can be referenced! ###
from langchain.memory import ConversationSummaryMemory, FileChatMessageHistory

load_dotenv()

# chat = ChatOpenAI()
# Comment the following and uncomment the above when the debug flag verbose=True not required
# The debug flag verbose=True shows conversation summaries generated for ConversationSummaryMemory as System messages when generating a new response.
chat = ChatOpenAI(verbose=True)

# memory = ConversationBufferMemory(
        # Whereas messages.json file acts as a DB that stores
        # old chats that can be referred to whenever the application is booted. The constructor FileChatMessageHistory automatically creates the file with the name provided to it as the input argument.
        # chat_memory=FileChatMessageHistory("messages.json"),
### The above was when using ConversationBufferMemory. The following is for ConversationSummaryMemory. As the name suggests, it uses its own prompt template and we have to provide it with a language model that it can use to summarise conversations while generating a new response. However, ConversationSummaryMemory takes longer to generate a response as it uses its own llm on top of the main llm being used. [ ] Maybe a comparison benchmark analysis can be performed? ###
memory = ConversationSummaryMemory(
        memory_key="messages", 
        return_messages=True,
        # chat variable is defined above that uses OpenAI's language model
        llm=chat
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

# [ ] Document the difference between prompt chain above and the following MAIN chain
chain = LLMChain(
        llm=chat,
        prompt=prompt,
        # Wiring the memory in
        memory=memory,
        # Debug flag to see how the language model is operating
        # comment the following when running the application normally
        verbose=True
        )

while True:
    content = input(">> ")

    result = chain({"content": content})

    print(result["text"])

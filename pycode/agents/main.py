from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
        ChatPromptTemplate,
        HumanMessagePromptTemplate,
        MessagesPlaceholder
        )

# Imports specific to agents.
# Agents: In short, similar to chains we have been using so
# far. Also includes the support of accepting various tools
# like the one we have defined to interact with an sqlite db.
# [ ] Include some description of agents in the README
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from dotenv import load_dotenv

# The following import is from a file created by us containing
# the specifics of the tool we want to use for this project.
# [ ] The README should contain some description around this
# link.
from tools.sql import run_query_tool

load_dotenv()

chat = ChatOpenAI()
prompt = ChatPromptTemplate(
        messages=[
            # Just the variable 'input' defines our
            # HumanMessagePromptTemplate in this case
            HumanMessagePromptTemplate.from_template("{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
            ]
        )

tools = [run_query_tool]

# Defining our agent's structure
agent = OpenAIFunctionsAgent(
        llm=chat,
        prompt=prompt,
        tools=tools
        )

agent_executor = AgentExecutor(
        # From the above defined agent
        agent=agent,
        verbose=True,
        tools=tools
        )

# In the following we make use of our agent_executor defined 
# above
agent_executor("How many users are in the database?")

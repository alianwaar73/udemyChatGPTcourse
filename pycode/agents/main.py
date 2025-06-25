from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
        ChatPromptTemplate,
        HumanMessagePromptTemplate,
        MessagesPlaceholder
        )

# Imports specific to agents.
# Agents: In short, similar to chains we have been using so
# far. Also includes the support for accepting various tools
# like the one we have defined to interact with an sqlite db.
# [ ] Include some description of agents in the README
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor

from langchain.memory import ConversationBufferMemory

# [ADDENDEM:] Post main_backup.py event for the system
# message approach
from langchain.schema import SystemMessage

from dotenv import load_dotenv

# The following import is from a file created by us containing
# the specifics of the tool we want to use for this project.
# [ ] The README should contain some description around this
# link.
# [ADDENDUM:] Modifying the following import for the system
# message apporach after the main_backup.py event
from tools.sql import run_query_tool, describe_tables_tool, list_tables
from tools.report import write_report_tool

load_dotenv()

chat = ChatOpenAI()

tables = list_tables()
# [DEBUG:] Uncomment for the following for debugging
# print(tables)

prompt = ChatPromptTemplate(
        messages=[
            # [ADDENDUM:] Drafting a detailed system message
            # so that ChatGPT does not assume stuff about the 
            # schema of our db
            # [PERSONAL NOTE:] Providing such a detailed 
            # SystemMessage in plain English, to me, is the 
            # perfect example of the highest-level coding. Or,            # personally I dread this term, the so called 
            # vibe coding.
            # SystemMessage(content=f"You are an AI that has access to an SQLite database.\n{tables}"),
            SystemMessage(content=(
                "You are an AI that can access a SQLite database.\n"
                f"The database has tables of: {tables}\n"
                "Do not make any assumptions about the schema of the database yourself. Always use the 'describe_tables' function"
                )),
            # Wiring in memory
            MessagesPlaceholder(variable_name="chat_history"),
            # Just the variable 'input' defines our
            # HumanMessagePromptTemplate in this case
            HumanMessagePromptTemplate.from_template("{input}"),
            # Grider refers to the agent_scratchpad as a simplified
            # form of memory. [ ] Need some custom, personalised
            # explanation. In short seems to handle inter-mediate
            # steps from a human-readable query/prompt to a relevant
            # function needed to execute an agent in the context of the 
            # tool, such as sqlite db, in the context of our application.
            MessagesPlaceholder(variable_name="agent_scratchpad")
            ]
        )

memory = ConversationBufferMemory(
        memory_key="chat_history",
        # The following returns memory objects
        # [REFERENCE:] Completion vs message-based messaging
        return_messages=True
        )

# [ADDENDUM:] Post main_backup.py event
tools = [
            run_query_tool, 
            describe_tables_tool,
            write_report_tool
        ]

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
        tools=tools,
        # Wiring in memory
        memory=memory
        )

# In the following we make use of our agent_executor defined 
# above
# [ ] <Investigation> The following query works given the 
# HUGE assumption made by the ChatGPT where it assumes a table
# named 'users' which happens to be there in our db. But fails
# when something like 'shipping address' is queried! Raising 
# the need to modifiy our sql.py (done) so that ChatGPT is
# context-aware about our db without making assumptions about
# its structure on its own! It seems to be a huge short-coming
# in it. It has also been observed in other use cases such as
# where it edits the code disregarding the naming conventions
# provided in a reference file! Although its logic stays
# correct!
# agent_executor("How many users are in the database?")

# Also, observing the output of the following query is VERY
# INSIGHTFUL! Shows the process in which the agent eventually
# figures out the way to correct interact with our db!!! [ ]
# Prompt-engineering display here, I think! I am just
# surprised at the fact that the agent keeps trying until it
# figures out the correct way to interact with the db along
# with determining its correct schema! [ ]Also, include in the
# README if this figuring out convergence is handled by the 
# agent_scratchpad?

# [IMPORTANT:] Agent scratchpad has a memory of its own
# to keep track of intermediate steps until it converges
# to an answer. BUT multiple calls to agent_executor does
# not preserve this temporary memory deployed by the 
# scratchpad. Only human and AI messages can be preserved
# and should be used with the conventional memory as used
# in the previous sections.

# Collection of different prompts that can be tried
# agent_executor("What is the most-used shipping address?")
agent_executor("How many users have provided a shipping address?")
# agent_executor("Most used user password?")
# agent_executor("List 6 unique user emails")
# agent_executor("Top 5 most ordered products? Write a report about it to a file.")
agent_executor("Top 20 most active users, their email and contact details, and individual products they ordered with their prices? Write a report about it to a file.")

# [IMPORTANT] This file is being backed up with the name 
# main_backup.py to preserve its current state for 
# reproducibility to observed how the above un-commented
# prompt behaves. main.py continues with the course in which
# the errors generated as a result of ChatGPT is handled by
# informing ChatGPT about our db in its system message. 
# [ ] Definitely a comparison can be studied between this 
# (what I call prompt engineering where one figures out a 
# prompt to provide which makes the agent work right. Or the 
# approach in the main.py
# [Addendum] Continuing with the course. Refer to 
# backups/main_backup.py for the [IMPORTANT] comment block
# along with its associated description in the README

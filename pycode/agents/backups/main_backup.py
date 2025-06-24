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
            # Grider refers to the agent_scratchpad as a simplified
            # form of memory. [ ] Need some custom, personalised
            # explanation. In short seems to handle inter-mediate
            # steps from a human-readable query/prompt to a relevant
            # function needed to execute an agent in the context of the 
            # tool, such as sqlite db, in the context of our application.
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
agent_executor("What is the most-used shipping address?")

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

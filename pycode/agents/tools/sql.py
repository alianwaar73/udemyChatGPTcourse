import sqlite3

# [ ] The README should contain a description of Tool. Why it 
# came into being and what purpose does it serve. Current
# understanding: It makes interacting with chatgpt easier and more
# structured specifically when stepping into the realm of agents.
from langchain.tools import Tool

# In the following line we make a connection to our sqlite db.
# This is stored in a file named db.sqlite.
conn = sqlite3.connect("db.sqlite")

# [ ] Some background on sqlite package specifically the variables
# used in the following such as what is "c" and general
# description of the following function in README
def run_sqlite_query(query):
    c = conn.cursor()
    c.execute(query)
    return c.fetchall()

# The following defines how to interact with chatgpt by making use
# of the function just defined above.
run_query_tool = Tool.from_function(
        # The following 'name' keyword cannot contain spaces
        name="run_sqlite_query",
        # This is in a way chatting with chatgpt through the
        # 'description' in the following. Another keyword
        description="Run a sqlite query.",
        func=run_sqlite_query
        )

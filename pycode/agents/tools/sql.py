import sqlite3

# [SOURCE MODIFICATION] The following two imports are to make some custom
# modifications to the source code of LangChain so that
# it communicates better with ChatGPT in order to make 
# ChatGPT does not assume stuff about the schema of our
# database. [REMEDY:] to the ChatGPT continuous assumptions 
# about the schema of our database. The problem was in the way
# LangChain was making our tools to communicate with ChatGPT.
from pydantic.v1 import BaseModel
from typing import List

# [ ] The README should contain a description of Tool. Why it 
# came into being and what purpose does it serve. Current
# understanding: It makes interacting with chatgpt easier and more
# structured specifically when stepping into the realm of agents.
from langchain.tools import Tool

# In the following line we make a connection to our sqlite db.
# This is stored in a file named db.sqlite.
conn = sqlite3.connect("db.sqlite")

# [ADDENDUM:] The following function is being added after the
# main_backup.py event. The purpose is to inform ChatGPT about
# our db schema in the main.py with a system message. Refer
# to the corresponding block in main.py for the context.
def list_tables():
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = c.fetchall()
#    return rows
    return "\n".join(row[0] for row in rows if row[0] is not None)

# [ ] Some background on sqlite package specifically the variables
# used in the following such as what is "c" and a general
# description of the following function in README
def run_sqlite_query(query):
    c = conn.cursor()
    try:
        c.execute(query)
        return c.fetchall()
    # If the above does not work then send the verbose error
    # off to ChatGPT to inform it to try something else.
    # The try: except has been added retrospectively after
    # realising that ChatGPT makes HUGE assumptions when
    # interacting with our sqlite db. It works for the simple
    # prompt such as "How many users are there?" but fails
    # when asked something like "How about their shipping 
    # addresses!" It signals that ChatGPT should know more
    # about our db in someway! One way to do that is to 
    # capture and then send an error, if it occurs, back 
    # to ChatGPT. [ ] Include an investigative discussion on
    # it in the README!
    except sqlite3.OperationalError as err:
        return f"The following error occurred while interacting with the sqlite db: {str(err)}"

# [SOURCE MODIFICATION:] The followin is added for the purpose# described at the start of the file.

class RunQueryArgsSchema(BaseModel):
    # [ ] It informs LangChain to use an argument called query    # which is a string instead of something like __arg1 (the
    # defaut case) in its source code.
    query: str

# The following defines how to interact with chatgpt by making# use of the function just defined above.
run_query_tool = Tool.from_function(
        # The following 'name' keyword cannot contain spaces
        name="run_sqlite_query",
        # This is in a way chatting with chatgpt through the
        # 'description' in the following. Another keyword
        description="Run a sqlite query.",
        func=run_sqlite_query,
        args_schema=RunQueryArgsSchema
        )

# [ADDENDUM:] Post main_backup.py event
def describe_tables(table_names):
    c = conn.cursor()
    tables = ', '.join("'" + table + "'" for table in table_names)
    rows = c.execute(f"SELECT sql FROM sqlite_master WHERE type='table' and name IN ({tables});")
    return '\n'.join(row[0] for row in rows if row[0] is not None)

# [SOURCE MODIFICATION:]
class DescribeTablesArgsSchema(BaseModel):
    table_names: List[str]

# Wrapping the above function into a reusable tool
describe_tables_tool = Tool.from_function(
        name="describe_tables",
        description="Given a list of table names, returns the schema of those tables",
        func=describe_tables,
        args_schema=DescribeTablesArgsSchema
        )

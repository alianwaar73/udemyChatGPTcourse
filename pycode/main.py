from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# The SequentialChain package is to connect two chains together
from langchain.chains import LLMChain, SequentialChain

# The following import is to secure the API key in a dotenv (.env) file
from dotenv import load_dotenv

# For input argument parsing from the command line
import argparse

# Loads the dotenv file containing the OPENAI API Key
load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--task", default="Return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()

llm = OpenAI()

# The following is for Chain A
code_prompt = PromptTemplate(
        input_variables=["language", "task"],
        template="Write a very short {language} function that will {task}."
        )

# The following is for Chain B
test_prompt = PromptTemplate(
        input_variables=["language", "code"],
        template="Write a test for the following {language} code:\n{code}"
        )

# Let us call the following Chain A
code_chain = LLMChain(
        llm=llm,
        prompt=code_prompt,
        # The following is to connect this Chain A to Chain B
        output_key="code"
        )

# Let us call the following Chain B
test_chain = LLMChain(
        llm=llm,
        prompt=test_prompt,
        output_key="test"
        )

# In the following we connect the above two chains together
# Listed inputs will be inputs to Chain A and listed outputs will be from Chain B

chain = SequentialChain(
        chains=[code_chain, test_chain],
        input_variables=["task", "language"],
        output_variables=["test", "code"]
        )

# On the command line the file can be run as the following example
# python main.py --language javascript --task 'print hello'
result = chain({
    "language": args.language,
    "task": args.task
    })

#result = llm("What is langchain, describe very briefly!")
print(">>>>>>>>>> GENERATED CODE:")
print(result["code"])

print(">>>>>>>>>> GENERATED TEST:")
print(result["test"])

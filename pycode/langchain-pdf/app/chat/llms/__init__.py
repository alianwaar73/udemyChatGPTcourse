# Whereas partial from functools is used to create a
# partial function that can be used to create an LLM
# instance. 
from functools import partial
from .chatopenai import build_llm

# The following is a dictionary that maps model names
# to their respective LLM creation functions.
# This allows for easy instantiation of different LLMs
# without needing to specify the model name each time. 

llm_map = {
    # Removed invalid/unreleased model to avoid random selection failures
    "gpt-4o": partial(build_llm, model_name="gpt-4o"),
    "gpt-3.5-turbo": partial(build_llm, model_name="gpt-3.5-turbo"),
}

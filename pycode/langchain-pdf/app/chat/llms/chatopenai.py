from langchain.chat_models import ChatOpenAI

# In order to make out build_llm more modular
# we can pass (language) model_name as an argument to it.
def build_llm(chat_args, model_name):
    return ChatOpenAI(
        streaming=chat_args.streaming,
        model_name=model_name
    )

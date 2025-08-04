# The following import is to allow users to randomly
# pick a retriever from the available ones.
import random

from app.chat.models import ChatArgs
from langchain.chat_models import ChatOpenAI

# Line 1 and build_chat was initiated with the package
# The rest has been added retroactively
# from app.chat.vector_stores.pinecone import build_retriever

# The import above is commented out in favor of the
# following import, in order to modularize the
# retrieval process and enable the choice of retriever.
from app.chat.vector_stores import retriever_map

# [FOLLOW UP: ADDENDUM: chat.py: ConversationalRetrievalChain]
# from langchain.chains import ConversationalRetrievalChain
# The above line is being commented out in favor of the 
# following, in order to enable streaming support to the
# ConversationalRetrievalChain and our application in turn.
# [REFERENCE: retrieval.py]
from app.chat.chains.retrieval import StreamingConversationalRetrievalChain

# from app.chat.llms.chatopenai import build_llm
# from app.chat.memories.sql_memory import build_memory

from app.chat.llms import llm_map
from app.chat.memories import memory_map

# The following import is a continuation of enabling
# modularity in the build_chat function. The purpose 
# of this import is to allow the retrieval of conversation
# components such as conversation_id, pdf_id, metadata,
# and streaming flag, which are necessary for building
# the chat chain of choice.
from app.web.api import (
    set_conversation_components,
    get_conversation_components
)

def select_component(
    component_type,
    component_map,
    chat_args
):
    components = get_conversation_components(
        chat_args.conversation_id
    )

    previous_component = components[component_type]

# If this is the first time the user is interacting
# with the chat, then a random component is chosen.
# If the user has interacted with the chat before,
# then the same component is used as before.
    if previous_component:
        builder = component_map[previous_component]
        return previous_component, builder(chat_args)
    else:
        random_name = random.choice(list(component_map.keys()))
        builder = component_map[random_name]
        return random_name, builder(chat_args)

# Adding modularity in order to enable the choice of 
# choosing the retriever, llm, and memory in our 
# build_chat function.
def build_chat(chat_args: ChatArgs):
    """
    :param chat_args: ChatArgs object containing
        conversation_id, pdf_id, metadata, and streaming flag.

    :return: A chain

    Example Usage:

        chain = build_chat(chat_args)
    """
    retriever_name, retriever = select_component(
        "retriever",
        retriever_map,
        chat_args
    )
    
    llm_name, llm = select_component(
        "llm",
        llm_map,
        chat_args
    )

    memory_name, memory = select_component(
        "memory",
        memory_map,
        chat_args
    )

    print(
        f"Running chat with llm: {llm_name}, memory: {memory_name}, retriever: {retriever_name}"
    )

    set_conversation_components(
        chat_args.conversation_id,
        llm=llm_name,
        retriever=retriever_name,
        memory=memory_name
    )

    # components = get_conversation_components(
    #     chat_args.conversation_id
    # )
    #
    # # The following retriever has been properly scoped.
    # # See pinecone.py and __init__.py for details on
    # # pdf_id used for scoping our custom retriever
    # # retriever = build_retriever(chat_args)
    #
    # # As initialized above, components contains a 
    # # dictionary with the retriever and other
    # # conversation components. The following line
    # # replaces the previous retriever initialization
    # # above.
    # previous_retriever = components["retriever"]
    #
    # retriever = None
    # if previous_retriever:
    #     # This gets executed if it is NOT the first time
    #     # the user is interacting with the chat. In this
    #     # case, same retriever is used as before.
    #     build_retriever = retriever_map[previous_retriever]
    #     retriever = build_retriever(chat_args)
    # else:
    #     # If this block is executed, it implies that 
    #     # this is the first time the user is
    #     # interacting with the chat. In this case, a 
    #     # random retriever can be chosen.
    #     random_retriever_name = random.choice(list(retriever_map.keys()))
    #     build_retriever = retriever_map[random_retriever_name]
    #     retriever = build_retriever(chat_args)
    #
    #     set conversation_components(
    #         conversation_id=chat_args.conversation_id,
    #         llm="",
    #         memory="",
    #         retriever=random_retriever_name
    #     )

    # llm = build_llm(chat_args)
    #
    # # [ ][JUAI:] Correting the behavior of followup 
    # # questions in my application.
    condense_question_llm = ChatOpenAI(streaming=False)
    # memory = build_memory(chat_args)
    #
#    return ConversationalRetrievalChain.from_llm(
# The following is the result of [FOLLOW UP: ADDENDUM: chat.py: ConversationalRetrievalChain]
    return StreamingConversationalRetrievalChain.from_llm(
            llm=llm,
            condense_question_llm=condense_question_llm,
            memory=memory,
            retriever=retriever
            )

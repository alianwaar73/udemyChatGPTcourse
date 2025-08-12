# The code contained inside this file is an improvement on the
# tchat project that utilised langchain's ChatMessageHistory.
# Instead it uses (modifies ChatMessageHistory) to
# SqlMessageHistory so that conversations persist for good.

# from pydantic import BaseModel
from langchain.memory import ConversationBufferMemory
from app.chat.memories.histories.sql_history import SqlMessageHistory
# from langchain.schema import BaseChatMessageHistory

# from app.web.api import (
#        get_messages_by_conversation_id,
#        add_message_to_conversation
#        )

# The following custom class extends BaseModel and 
# BaseChatMessageHistory

# [Section 13:] The following class is moved to histories/
# sql_message_history.py.

# class SqlMessageHistory(BaseChatMessageHistory, BaseModel):
#     conversation_id: str
#
#     # [ ] The following syntax is new to me. JUAI for it.
#     @property
#     def messages(self):
#         return get_messages_by_conversation_id(self.conversation_id)
#
#     def add_message(self, message):
#         return add_message_to_conversation(
#                 conversation_id=self.conversation_id,
#                 role=message.type,
#                 content=message.content
#                 )
#
#     # The following function, in our particular case of a
#     # custom class does nothing. Has meaning in the class we
#     # are extending (ChatMessageHistory).
#     def clear(self):
#         pass

# The following defines our custom memory for our application
# that makes use of SqlMessageHistory
def build_memory(chat_args):
    return ConversationBufferMemory(
            chat_memory=SqlMessageHistory(
                conversation_id=chat_args.conversation_id
                ),
            return_messages=True,
            memory_key="chat_history",
            output_key="answer"
            )


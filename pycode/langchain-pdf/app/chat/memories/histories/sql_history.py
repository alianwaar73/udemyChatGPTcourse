from pydantic import BaseModel
from langchain.schema import BaseChatMessageHistory

from app.web.api import (
    get_messages_by_conversation_id,
    add_message_to_conversation
)

class SqlMessageHistory(BaseChatMessageHistory, BaseModel):
    conversation_id: str
    
    # [ ] The following syntax is new to me. JUAI for it.
    @property
    def messages(self):
        return get_messages_by_conversation_id(self.conversation_id)
    
    def add_message(self, message):
        return add_message_to_conversation(
                conversation_id=self.conversation_id,
                role=message.type,
                content=message.content
                )

    # The following function, in our particular case of a
    # custom class does nothing. Has meaning in the class we
    # are extending (ChatMessageHistory).
    def clear(self):
        pass



# [SOURCE CODE INTERACTION]
from langchain.callbacks.base import BaseCallbackHandler

# Following import to make output rendered nicely within
# colored boxes
from pyboxen import boxen

# Helper function to make the best use of the boxen package
def boxen_print(*args, **kwargs):
    print(boxen(*args, **kwargs))

class ChatModelStartHandler(BaseCallbackHandler):
    def on_chat_model_start(self, serialized, messages, **kwargs):
#        print("\n\n\n\n========== Sending messages ==========\n\n")
        boxen_print(f"Sending messages ...", color="white")
        # messages is a list of lists
        for message in messages[0]:
            if message.type == "system":
                boxen_print(message.content, title=message.type, color="yellow")

            elif message.type == "human":
                boxen_print(message.content, title=message.type, color="green")

            # [ ] Ask the AI in detail about the following one            # in README
            elif message.type == "ai" and "function_call" in message.additional_kwargs:
                call = message.additional_kwargs["function_call"]
                boxen_print(
                        f"Running tool {call['name']} with args {call['arguments']}", 
                        title=message.type, 
                        color="cyan"
                        )

            elif message.type == "ai":
                boxen_print(message.content, title=message.type, color="blue")

            elif message.type == "function":
                boxen_print(message.content, title=message.type, color="purple")

            else:
                boxen_print(message.content, title=message.type)

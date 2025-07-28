# The following import is required to set the application
# context. It is a requirement by the flask application in
# order for it to function properly with out website.
# The following import affects how Thread() is called below.
# Specifically an argument of args is specificied.
from flask import current_app

from queue import Queue
from threading import Thread
from app.chat.callbacks.stream import StreamingHandler

class StreamableChain:
    def stream(self, input):
        # If used as is the self(input) part keeps waiting
        # until the queue on OpenAI is all filled up. That
        # the langchain-side limitation. It does not move
        # ahead to the while loop. So this way streaming
        # is an illusion.
        # [JUAI:] In order to solve this, concurrency is 
        # used bY making use of threads. It is not 
        # parallelism. [ ] README should address this.

        # [ADDENDUM FOLLOW UP:] Creating separate instances
        # of Queue and StreamingHandler to address the issue
        # of separate users using their own dedicated
        # corresponding instance of Queue and 
        # StreamingHandler
        queue = Queue()
        handler = StreamingHandler(queue)

        def task(app_context): # See the start of the file for the reason of adding app_context argument here.
            # [ ][POST ADDENDUM:][JUAI:]
            # self(input)
            app_context.push()
            self(input, callbacks=[handler])

        Thread(
            target=task,
            args=[current_app.app_context()] # Refer to the start of the file, flask import, to see details associated with this line.
        ).start()
        # The following creates a generator that will be
        # iterated over to implement streaming. *yield*
        # is the keyword to do it. Such as:
        # yield 'hi'
        # yield 'there'
        # Reading the values from the queue populated above
        # with the stream coming from OpenAI side
        while True:
            token = queue.get()
            if token is None:
                break
            yield token



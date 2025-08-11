# This file is to store and manage component scores in Redis.
# Components such as llm, pinecone, and memory.

import os
import redis

client = redis.Redis.from_url(
    os.environ["REDIS_URI"],
    decode_responses=True
)

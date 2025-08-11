# Currently, entire conversations are scored. The purpose is
# to determine the best LLM, retriever, and memory 
# combination. [IMPROVEMENT:] In my opinion, individual
# prompt-response score should be taken into account. 
# That would involve, in my opinion, tweaking the actual
# LLM and other components. Something, to look into later 
# for research.
import random
from app.chat.redis import client

def random_component_by_score(component_type, component_map):
    if component_type not in ["llm", "retriever", "memory"]:
        raise ValueError("Invalid component type. Must be 'llm', 'retriever', or 'memory'.")

    values = client.hgetall(f"{component_type}_score_values")
    counts = client.hgetall(f"{component_type}_score_counts")

    # print(values, counts)

    names = component_map.keys()

    avg_scores = {}
    for name in names:
        # We assume that if the component does not have
        # a score, it defaults to 1. int is used here
        # because redis stores everything as strings.
        score = float(values.get(name, 1.0))
        count = int(counts.get(name, 1))

        avg = score / count 
        # Ensure the average score is at least 0.1
        # to cover a corner case where a user downvotes
        # a component on the first use. Otherwise, the
        # component will not be used again.
        avg_scores[name] = max(avg, 0.1)

    # print(avg_scores)
    sum_scores = sum(avg_scores.values())
    random_val = random.uniform(0, sum_scores)
    cumulative = 0

    # In the following a weighted random choice is made
    # based on the average scores of the components.
    # The component with the highest average score is more 
    # likely to be chosen.
    for name, score in avg_scores.items():
        cumulative += score
        if random_val <= cumulative:
            return name

def score_conversation(
    conversation_id: str, score: float, llm: str, retriever: str, memory: str
) -> None:
    """
    [LEGACY COMMENT BY THE INSTRUCTOR:]
    This function interfaces with [ ]langfuse to assign a score to a conversation, specified by its ID.
    It creates a new langfuse score utilizing the provided llm, retriever, and memory components.
    The details are encapsulated in JSON format and submitted along with the conversation_id and the score.

    :param conversation_id: The unique identifier for the conversation to be scored.
    :param score: The score assigned to the conversation.
    :param llm: The Language Model component information.
    :param retriever: The Retriever component information.
    :param memory: The Memory component information.

    Example Usage:

    score_conversation('abc123', 0.75, 'llm_info', 'retriever_info', 'memory_info')
    """
# A clever way to get the score in my opinion. A clever
# way of using a combination of min max as follows
    score = min(max(score, 0), 1)

# In order to determine the average, individual scores 
# along with their count are stored in Redis as follows for 
# the three components: llm, retriever, and memory.

# The following six lines correspond to the six Redis hash 
# tables

    client.hincrbyfloat("llm_score_values", llm, float(score))
    client.hincrby("llm_score_counts", llm, 1)

    client.hincrbyfloat("retriever_score_values", retriever, float(score))
    client.hincrby("retriever_score_counts", retriever, 1)

    client.hincrbyfloat("memory_score_values", memory, float(score))
    client.hincrby("memory_score_counts", memory, 1)

def get_scores():
    """
    Retrieves and organizes scores from the langfuse client for different component types and names.
    The scores are categorized and aggregated in a nested dictionary format where the outer key represents
    the component type and the inner key represents the component name, with each score listed in an array.

    The function accesses the langfuse client's score endpoint to obtain scores.
    If the score name cannot be parsed into JSON, it is skipped.

    :return: A dictionary organized by component type and name, containing arrays of scores.

    Example:

        {
            'llm': {
                'chatopenai-3.5-turbo': [score1, score2],
                'chatopenai-4': [score3, score4]
            },
            'retriever': { 'pinecone_store': [score5, score6] },
            'memory': { 'persist_memory': [score7, score8] }
        }
    """

    result = {}

    for component_type in ("llm", "retriever", "memory"):
        values = client.hgetall(f"{component_type}_score_values")
        counts = client.hgetall(f"{component_type}_score_counts")

        names = set(values.keys()) | set(counts.keys())
        result[component_type] = {}
        for name in names:
            total = float(values.get(name, 0.0))
            count = int(counts.get(name, 0))
            avg = (total / count) if count > 0 else 0.0
            result[component_type][name] = {
                "avg": avg,
                "count": count,
                "sum": total,
            }

    return result

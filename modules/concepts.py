"""
concepts.py
Reference concepts for VBCUA
"""

CONCEPTS = {

    "Machine Learning":
    """
    Machine Learning is a branch of Artificial Intelligence that enables
    computers to learn from data without being explicitly programmed.
    It uses algorithms to identify patterns, make predictions,
    and improve performance through experience.
    """,

    "Cloud Computing":
    """
    Cloud Computing is the delivery of computing services such as
    servers, storage, databases, networking, software,
    and analytics over the Internet.
    It provides scalability, flexibility,
    and cost-effective resource management.
    """,

    "Artificial Intelligence":
    """
    Artificial Intelligence is the simulation of human intelligence
    in machines that are capable of learning,
    reasoning, problem solving,
    and decision making.
    AI includes machine learning,
    natural language processing,
    and computer vision.
    """,

    "Data Science":
    """
    Data Science is an interdisciplinary field
    that combines statistics,
    machine learning,
    programming,
    and domain knowledge
    to extract useful insights from data.
    """,

    "Internet of Things":
    """
    The Internet of Things refers to
    interconnected physical devices
    that communicate over the internet,
    collect data,
    and automate various tasks.
    """
}


def get_topics():
    """
    Return list of topics.
    """
    return list(CONCEPTS.keys())


def get_reference(topic):
    """
    Return reference explanation.
    """
    return CONCEPTS.get(topic, "")
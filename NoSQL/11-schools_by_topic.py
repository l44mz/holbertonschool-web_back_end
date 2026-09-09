#!/usr/bin/env python3
"""
11-schools_by_topic.py
Module that contains a function to return the list of schools
having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: the pymongo collection object
        topic (str): the topic searched

    Returns:
        A list of documents (schools) that have the given topic
        in their 'topics' field.
    """
    documents = mongo_collection.find({"topics": topic})
    return [doc for doc in documents]

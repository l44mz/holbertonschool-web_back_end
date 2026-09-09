#!/usr/bin/env python3
"""
8-all.py
Module that contains a function to list all documents in a collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    Args:
        mongo_collection: the pymongo collection object

    Returns:
        A list of documents, or an empty list if there are none.
    """
    documents = mongo_collection.find()
    return [doc for doc in documents]

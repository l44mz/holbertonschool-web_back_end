#!/usr/bin/env python3
"""
9-insert_school.py
Module that contains a function to insert a new document
in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: the pymongo collection object
        **kwargs: key/value pairs representing the document fields

    Returns:
        The new document's _id.
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id

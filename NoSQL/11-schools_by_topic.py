#!/usr/bin/env python3
""" MongoDB Operations with Python """


def schools_by_topic(mongo_collection, topic):
    """ returns the list """
    documents = mongo_collection.find({"topics": topic})
    list_docs = [d for d in documents]
    return list_docs

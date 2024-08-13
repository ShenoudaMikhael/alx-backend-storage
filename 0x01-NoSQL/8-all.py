#!/usr/bin/env python3
""" 8-main """


def list_all(mongo_collection):
    """list_all function"""
    return mongo_collection.find()

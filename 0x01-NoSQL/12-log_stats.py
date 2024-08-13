#!/usr/bin/env python3
"""12-Log_stats"""


from pymongo import MongoClient


def log_stats():
    """log_stats function"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    logs_collection = client.logs.nginx
    total = logs_collection.count_documents({})
    get = logs_collection.count_documents({"method": "GET"})
    post = logs_collection.count_documents({"method": "POST"})
    put = logs_collection.count_documents({"method": "PUT"})
    patch = logs_collection.count_documents({"method": "PATCH"})
    delete = logs_collection.count_documents({"method": "DELETE"})
    path = logs_collection.count_documents({"method": "GET", "path": "/status"})
    print("{} logs".format(total))
    print("Methods:")
    print("\tmethod GET: {}".format(get))
    print("\tmethod POST: {}".format(post))
    print("\tmethod PUT: {}".format(put))
    print("\tmethod PATCH: {}".format(patch))
    print("\tmethod DELETE: {}".format(delete))
    print("{} status check".format(path))


if __name__ == "__main__":
    log_stats()

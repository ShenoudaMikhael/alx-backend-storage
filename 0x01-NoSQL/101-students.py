#!/usr/bin/env python3
"""101-students"""


def top_students(mongo_collection):
    """top_students function"""
    result = mongo_collection.aggregate(
        [
            {"$project": 
             {"name": "$name", "averageScore": {"$avg": "$topics.score"}}},
            {"$sort": {"averageScore": -1}},
        ]
    )
    return result

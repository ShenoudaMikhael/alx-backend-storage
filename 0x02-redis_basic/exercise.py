#!/usr/bin/env python3
"""exercise"""
import uuid
from typing import Union
import redis


class Cache:
    """Cache class"""

    def __init__(self):

        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store function"""
        key = str(uuid.uuid4())

        self._redis.set(key, data)
        return key

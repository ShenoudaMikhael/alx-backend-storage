#!/usr/bin/env python3
"""exercise"""
from typing import Union
import redis
import uuid


class Cache:
    """Cache class"""

    def __init__(self):

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, float, bytes]) -> str:
        """store function"""
        key = str(uuid.uuid4())

        self._redis.mset({key: data})
        return key

#!/usr/bin/env python3
"""web.py"""
from functools import wraps
from typing import Callable
import requests
import redis


redis_instance = redis.Redis()


def data_cache(method: Callable) -> Callable:
    """data_cacher function"""

    @wraps(method)
    def wrapper(url) -> str:
        """wrapper function"""
        redis_instance.incr("count:{}".format(url))
        result = redis_instance.get("result:{}".format(url))
        if result:
            return result.decode("utf-8")
        result = method(url)
        redis_instance.set("count:{}".format(url), 0)
        redis_instance.setex("result:{}".format(url), 10, result)
        return result

    return wrapper


@data_cache
def get_page(url: str) -> str:
    """get_page function"""
    re = requests.get(url, timeout=30)
    return re.text

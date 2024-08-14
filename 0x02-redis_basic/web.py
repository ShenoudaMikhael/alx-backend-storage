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
        """wrapper method"""
        ckey = "cached:{}".format(url)
        cfata = redis_instance.get(ckey)
        if cfata:
            return cfata.decode("utf-8")

        counter = "count:{}".format(url)
        text = method(url)

        redis_instance.incr(counter)
        redis_instance.set(ckey, text)
        redis_instance.expire(ckey, 10)
        return text

    return wrapper


@data_cache
def get_page(url: str) -> str:
    """get_page function"""
    re = requests.get(url, timeout=30)
    return re.text

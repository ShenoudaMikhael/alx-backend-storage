#!/usr/bin/env python3
"""exercise"""
import uuid
from typing import Union, Callable, Any
from functools import wraps
import redis


def replay(fn: Callable) -> None:
    """replay function"""
    if fn is None or not hasattr(fn, '__self__'):
        return
    redis_store = getattr(fn.__self__, '_redis', None)
    if not isinstance(redis_store, redis.Redis):
        return
    key_in = '{}:inputs'.format(fn.__qualname__)
    key_out = '{}:outputs'.format(fn.__qualname__)
    fn_ccount = 0
    if redis_store.exists(fn.__qualname__) != 0:
        fn_ccount = int(redis_store.get(fn.__qualname__))
    print('{} was called {} times:'.format(fn.__qualname__, fn_ccount))
    f_inputs = redis_store.lrange(key_in, 0, -1)
    f_outputs = redis_store.lrange(key_out, 0, -1)
    for finput, foutput in zip(f_inputs, f_outputs):
        print('{}(*{}) -> {}'.format(
            fn.__qualname__,
            finput.decode("utf-8"),
            foutput,
        ))


def count_calls(method: Callable) -> Callable:
    """count_calls function"""
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper method"""
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwds)

    return wrapper


def call_history(method: Callable) -> Callable:
    """call_history function"""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """wrapper function"""
        key_in = '{}:inputs'.format(method.__qualname__)
        key_out = '{}:outputs'.format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(key_in, str(args))
        out = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(key_out, out)
        return out
    return wrapper


class Cache:
    """Cache class"""

    def __init__(self):

        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store function"""
        key = str(uuid.uuid4())

        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Callable = None
            ) -> Union[str, bytes, int, float]:
        """get function"""
        result = self._redis.get(key)
        return fn(result) if fn is not None else result

    def get_str(self, key: str) -> str:
        """get_str function"""
        return self.get(key, str)

    def get_int(self, key: int) -> int:
        """get_int function"""
        return self.get(key, int)


# if __name__ == "__main__":
#     cache = Cache()

#     TEST_CASES = {b"foo": None, 123: int, "bar": lambda d: d.decode("utf-8")}

#     for value, fn in TEST_CASES.items():
#         key = cache.store(value)
#         assert cache.get(key, fn=fn) == value

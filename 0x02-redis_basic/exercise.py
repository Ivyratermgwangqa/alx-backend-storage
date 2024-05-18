#!/usr/bin/env python3
"""
Redis Basic Operations

This module provides a Cache class for performing basic Redis operations.

Classes:
    Cache: A class for interacting with a Redis database.
    count_calls: A decorator to count number of times method is called.
    call_history: A decorator to store the history of inputs and outputs.
    replay: A function to display the call history of a decorated method.
"""

import redis
import uuid
from typing import Union, Callable, Optional
import functools


def count_calls(method: Callable) -> Callable:
    """
    A decorator that counts the number of times a method is called.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The wrapped method with call counting.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    A decorator that stores the history of inputs and outputs for method.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The wrapped method with input/output history storage.
    """
    inputs_key = method.__qualname__ + ":inputs"
    outputs_key = method.__qualname__ + ":outputs"

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(inputs_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(result))
        return result

    return wrapper


def replay(method: Callable):
    """
    Display the history of calls of a particular method.

    Args:
        method (Callable): The decorated method to replay the history for.
    """
    redis_instance = method.__self__._redis
    inputs_key = method.__qualname__ + ":inputs"
    outputs_key = method.__qualname__ + ":outputs"
    inputs = redis_instance.lrange(inputs_key, 0, -1)
    outputs = redis_instance.lrange(outputs_key, 0, -1)
    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for inp, out in zip(inputs, outputs):
        inp_decoded = inp.decode('utf-8')
        out_decoded = out.decode('utf-8')
        print(f"{method.__qualname__}(*{inp_decoded}) -> {out_decoded}")


class Cache:
    """
    A class for interacting with a Redis database.

    Methods:
        __init__: Initialize the Redis client and flush the database.
        store: Store data in Redis and return the generated key.
        get: Retrieve data from Redis and optionally convert it using callable.
        get_str: Retrieve data as a UTF-8 string.
        get_int: Retrieve data as an integer.
    """
    def __init__(self):
        """
        Initialize  Cache instance by setting Redis.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis and return the generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and optionally convert it using callable.

        Args:
            key (str): The key under which the data is stored.
            fn (Optional[Callable]): A callable to convert the data.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data as a UTF-8 string.

        Args:
            key (str): The key under which the data is stored.

        Returns:
            Optional[str]: The retrieved data as a string.
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data as an integer.

        Args:
            key (str): The key under which the data is stored.

        Returns:
            Optional[int]: The retrieved data as an integer.
        """
        return self.get(key, int)


# Testing the implementation
if __name__ == "__main__":
    cache = Cache()
    cache.store("foo")
    cache.store("bar")
    cache.store(42)
    replay(cache.store)

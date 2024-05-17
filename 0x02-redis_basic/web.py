#!/usr/bin/env python3
"""
Web cache and URL tracker

This module provides function to fetch & cache web pages with access tracking
using Redis.

Functions:
    get_page: Fetch the HTML content of URL, cache it, and track access count.
"""

import requests
import redis
from typing import Callable

# Create a Redis client
r = redis.Redis()


def count_access(method: Callable) -> Callable:
    """
    A decorator that counts the number of accesses to a URL.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The wrapped method with access counting.
    """
    def wrapper(url: str) -> str:
        r.incr(f"count:{url}")
        return method(url)
    return wrapper


@count_access
def get_page(url: str) -> str:
    """
    Fetch the HTML content of a URL, cache it, and track access count.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    cached_page = r.get(f"cache:{url}")
    if cached_page:
        return cached_page.decode('utf-8')
    response = requests.get(url)
    html_content = response.text
    r.setex(f"cache:{url}", 10, html_content)
    return html_content


# Testing the implementation
if __name__ == "__main__":
    test_url = (
        "http://slowwly.robertomurray.co.uk/delay/5000/url/"
        "http://www.example.com"
    )
    print(get_page(test_url))  # Fetches from the web and caches
    print(get_page(test_url))  # Should return the cached content
    print(get_page(test_url))  # Should return the cached content
    access_count = r.get(f'count:{test_url}').decode('utf-8')
    print(f"Access count for {test_url}: {access_count}")

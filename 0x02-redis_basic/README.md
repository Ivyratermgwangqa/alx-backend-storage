# 0x02. Redis basic

This project provides a simple Python module to fetch web pages, cache their content with Redis, and track the number of accesses to each URL.

## Features

- Fetches the HTML content of a URL using the `requests` module.
- Caches the content in Redis with an expiration time of 10 seconds.
- Tracks the number of accesses to each URL in Redis.

## Requirements

- Python 3.7 or higher
- Redis server
- `requests` module
- `redis` module

## Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <repository_name>
   ```

2. Install the required modules:
   ```sh
   pip3 install -r requirements.txt
   ```

3. Start the Redis server if not already running:
   ```sh
   service redis-server start
   ```

## Usage

1. Import the `get_page` function from the `web` module.
   ```python
   from web import get_page
   ```

2. Use the `get_page` function to fetch the HTML content of a URL.
   ```python
   url = "http://example.com"
   html_content = get_page(url)
   print(html_content)
   ```

## Testing

To test the functionality of the module, you can run the `web.py` script directly:
```sh
./web.py
```

This script fetches a sample URL, caches the content, and tracks the access count.

## License

This project is licensed under the [MIT License](LICENSE).
```

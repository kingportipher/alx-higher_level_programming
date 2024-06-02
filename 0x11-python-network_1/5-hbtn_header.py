#!/usr/bin/python3
"""
Sends a request to the URL and displays the value of the variable X-Request-Id
in the response header
"""

if __name__ == '__main__':
    from requests import get
    from sys import argv

    # Send GET request to the URL provided as command-line argument
    response = get(argv[1])

    # Retrieve and print the value of 'X-Request-Id' from the response headers
    print(response.headers.get('X-Request-Id'))

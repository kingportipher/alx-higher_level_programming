#!/usr/bin/python3
"""
Sends a POST request to the given URL with the email as a parameter,
and displays the body of the response.
"""

if __name__ == '__main__':
    from sys import argv
    from requests import post

    url = argv[1]
    email = argv[2]

    # Send POST request to the specified URL with email as a parameter
    response = post(url, data={'email': email})

    # Print the body of the response
    print(response.text)

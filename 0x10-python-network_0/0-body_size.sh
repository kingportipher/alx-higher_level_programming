#!/bin/bash
#a Bash script that takes in a URL, sends a request to that URL, 
#and displays the size of the body of the response

# Check if the URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request using curl and get the size of the response body
body_size=$(curl -sI "$1" | grep -i '^Content-Length:' | awk '{print $2}')

# Display the size of the response body in bytes
echo "$body_size"

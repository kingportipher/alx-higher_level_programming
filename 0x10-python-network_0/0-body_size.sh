#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# URL provided as argument
URL=$1

# Send request to URL and store response body in a temporary file
response=$(curl -s -w "%{size_download}" -o /tmp/response_body "$URL")

# Check if curl command was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to fetch data from $URL"
    exit 1
fi

# Display the size of the response body in bytes
echo "Size of the response body: $response bytes"

# Clean up temporary file
rm /tmp/response_body

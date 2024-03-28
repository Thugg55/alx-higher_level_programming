#!/usr/bin/python3
# Script to send request to a URL and output size of the body of the response
curl -sI "$1" | grep Content-Length | cut -d ' ' -f2

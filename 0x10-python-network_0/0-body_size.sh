#!/bin/bash
# Script to send request to a URL and displays size of the body
curl -sI "$1" | grep Content-Length | cut -d ' ' -f2

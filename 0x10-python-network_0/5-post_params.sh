#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1
email="test@gmail.com"
subt="I will always be here for PLD"

# Send POST request with specific parameters and display the response body
response=$(curl -s -X POST "$url" -d "email=$email" -d "subjt=$subject")
echo "$response"


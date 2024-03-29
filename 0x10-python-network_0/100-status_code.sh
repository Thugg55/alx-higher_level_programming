#!/bin/bash
# Script sends a request to a URL, displays status code
curl -s -o /dev/null -w "%{http_code}" "$1"

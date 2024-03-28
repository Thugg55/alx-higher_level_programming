#!/bin/bash
# Script sends a delete requestto the URL passed as the first argument
curl -sX DELETE "$1"

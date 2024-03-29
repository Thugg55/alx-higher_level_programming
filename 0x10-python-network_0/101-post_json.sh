#!/bin/bash
# Script POST JSON file
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"

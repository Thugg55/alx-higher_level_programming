#!/bin/bash
# Script takes in a URL as an argument
# Sends a GET request to the URL and displays the body 
curl -sLH "X-School-User-Id: 98" "$1"

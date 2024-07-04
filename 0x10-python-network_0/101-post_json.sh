#!/bin/bash
# Send a JSON POST request with the file contents
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"

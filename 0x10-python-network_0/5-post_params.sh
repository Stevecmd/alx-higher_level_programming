#!/bin/bash
# Sends a POST request to the passed URL with email and subject variables and displays the body of the response
curl -sX POST -d email=test@gmail.com -d subject="I will always be here for PLD" "$1"

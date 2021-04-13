#!/bin/bash
# takes a URL and sends a POST request to the URL
curl -s -X -H POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"

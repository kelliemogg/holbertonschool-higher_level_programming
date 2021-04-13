#!/bin/bash
# size of the body of the url
curl -s -I "$1" | grep -i Content-Length | awk '{print $2}' 

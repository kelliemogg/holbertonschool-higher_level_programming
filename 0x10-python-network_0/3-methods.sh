#!/bin/bash
# displays all http methods
curl -s -I "$1" | grep "Allow:"

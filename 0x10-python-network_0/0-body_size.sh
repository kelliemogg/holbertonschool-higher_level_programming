#!/bin/bash
# size of the body of the url
curl -sI "\n%{size_download}\n" $1 | wc -c

#!/bin/bash
curl -sI "$1"| wc -c
curl -sw "\n%{size_download}\n" $1 | tail -1

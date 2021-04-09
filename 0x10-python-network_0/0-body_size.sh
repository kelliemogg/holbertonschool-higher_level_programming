#!/bin/bash
curl -sI "\n%{size_download}\n" $1 | wc -c

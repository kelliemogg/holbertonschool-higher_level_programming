#!/bin/bash
# status code
curl -0 /dev/null --silent --head --write-out '%{http_code}\n'

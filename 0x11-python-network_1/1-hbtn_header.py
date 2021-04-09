#!/usr/bin/python3
""" script to take in a url, send a request to the URL, and
displays the value of the X-Request-Id variable """


import urllib.request
import sys

url = sys.argv[1]

if url is not None:
    with urllib.request.urlopen(url) as response:
        page = response.info()
        print(page.get("X-Request-ID"))

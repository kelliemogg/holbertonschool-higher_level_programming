#!/usr/bin/python3
""" fetches a website using requests packages """

import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]

    r = requests.get(url)
    if r.status_code < 400:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))





    
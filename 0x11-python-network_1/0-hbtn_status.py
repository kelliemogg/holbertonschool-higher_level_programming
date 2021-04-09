#!/usr/bin/python3
""" this module is to request data about a URL """


import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(str(html)))
    print("\t- utf8 content: {}".format(html.decode('UTF-8')))

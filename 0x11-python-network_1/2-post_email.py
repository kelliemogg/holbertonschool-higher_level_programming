#!/usr/bin/python3
""" script to take in a url, send a request to the URL, and
displays the value of the X-Request-Id variable """

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    data = {}
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    data = urllib.parse.urlencode(data)
    data = data.encode('UTF-8')
    req = urllib.request.Request(url, email)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print(page.decode('UTF-8'))

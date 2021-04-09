#!/usr/bin/python3
""" script to take in a url, send a request to the URL, and
displays the value of the X-Request-Id variable """

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import urllib.error
    import sys

    url = sys.argv[1]

    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            page = response.read()
            print(page.decode('UTF-8'))
    except urllib.error.URLError as res:
        print('Error code: {}'.format(res.code))

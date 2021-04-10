#!/usr/bin/python3
""" fetches a website using requests packages """

import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print('No result')
    else:
        q = sys.argv[1]
        l_d = {"q": q}
        url = 'http://0.0.0.0:5000/search_user'
        r = requests.post(url, l_d)
        try:
            jason = r.json()
            if jason == {}:
                print('No result')
            else:
                print('[{}] {}'.format(jason['id'], jason['name']))
        except:
            print('Not a valid JSON')

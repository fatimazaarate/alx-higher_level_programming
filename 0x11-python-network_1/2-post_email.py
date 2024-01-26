#!/usr/bin/python3
"""a Python script that takes in a URL
sends a request to the URL and displays the body of the response
"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(value).encode("utf-8")
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print(f"Your email is: {page.decode('utf-8')}")

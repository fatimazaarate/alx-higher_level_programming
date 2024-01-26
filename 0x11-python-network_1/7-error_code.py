#!/usr/bin/python3
"""a Python script that takes in a URL sends a request
to the URL and displays the body of the response
"""

import requests
import requests.exceptions
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        req = requests.get(url)
    except requests.exceptions.HTTPError as e:
        print("Error code:", e.code)
    else:
        print(req.text)

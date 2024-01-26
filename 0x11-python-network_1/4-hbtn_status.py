#!/usr/bin/python3
"""a Python script that takes in a URL sends a request
to the URL and displays the body of the response
"""

import requests


r = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print(f"\ttype: {type(r.headers['content-type'])}")
print(f"\tcontent: {r.text}")

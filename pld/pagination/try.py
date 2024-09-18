#!/usr/bin/env python3

import requests

data = requests.get('https://jsonplaceholder.typicode.com/users/')
print(data.json())

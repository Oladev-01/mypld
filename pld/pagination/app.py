#!/usr/bin/env python3
"""pagination session"""
from flask import Flask, request, jsonify
from typing import Dict, List, Union
import requests
import math
# ------- start of function ---------
def paginator(in_data: Union[List, Dict], index: int = None, page_size: int = 10) -> Dict:
    """paginator"""
    # ensure data is parsed to the function
    assert in_data is not None and index < len(in_data)
    # start call
    data = []
    # -------- start initial plan -------

    data_cpy = in_data
    del_keys = []
    # user deletes a data from the database:
    for _ in sorted(data_cpy.keys()):
        for child_key in sorted(in_data.keys()):
            if child_key not in data_cpy:
                del_keys.append(child_key)
    # -------- end initial plan --------
    # return in_data[start:end]
    next_index = index
    while len(data) <= page_size and next_index < len(in_data):
        if next_index in in_data:
            data.append(in_data[next_index])
        next_index += 1

    return {
        'index': index,
        'data': data,
        'page_size': page_size,
        'next_index': next_index
    }

# -------- end of function ----------
# page = 3 and page_size = 20, the end is 3*20 = 60
app = Flask(__name__)
"""
Users = [
    {'id': 1, 'name': 'User 1'},
    {'id': 2, 'name': 'User 2'},
    {'id': 3, 'name': 'User 3'},
    {'id': 4, 'name': 'User 4'},
    {'id': 5, 'name': 'User 5'},
    {'id': 6, 'name': 'User 6'},
    {'id': 7, 'name': 'User 7'},
    {'id': 8, 'name': 'User 8'},
    {'id': 9, 'name': 'User 9'},
    {'id': 10, 'name': 'User 10'},
    {'id': 11, 'name': 'User 11'},
    {'id': 12, 'name': 'User 12'},
    {'id': 13, 'name': 'User 13'},
    {'id': 14, 'name': 'User 14'}
]"""

posts = [
    {'id': 1, 'name': 'Posts 1'},
    {'id': 2, 'name': 'Posts 2'},
    {'id': 3, 'name': 'Posts 3'},
    {'id': 4, 'name': 'Posts 4'},
    {'id': 5, 'name': 'Posts 5'},
    {'id': 6, 'name': 'Posts 6'},
    {'id': 7, 'name': 'Posts 7'},
    {'id': 8, 'name': 'Posts 8'},
    {'id': 9, 'name': 'Posts 9'},
    {'id': 10, 'name': 'Posts 10'},
    {'id': 11, 'name': 'Posts 11'},
    {'id': 12, 'name': 'Posts 12'},
    {'id': 13, 'name': 'Posts 13'},
    {'id': 14, 'name': 'Posts 14'}
]

@app.route('/users', strict_slashes=False)
def get_users() -> Dict:
    """get users"""
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 5))
    Users = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    return jsonify(paginator(Users, page, limit))
    
@app.route('/posts', strict_slashes=False)
def get_posts() -> Dict:
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 5))
    todo = requests.get('https://jsonplaceholder.typicode.com/users/1/todos').json()
    return jsonify(paginator(todo, page, limit))
    return jsonify(paginator(posts, page, limit))


if __name__ == '__main__':
    app.run(debug=True)

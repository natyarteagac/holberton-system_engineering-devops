#!/usr/bin/python3
""" Export to CSV """

import csv
import json
import requests
from sys import argv

if __name__ == '__main__':
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".
        format(argv[1])).json()
    name_of_employee = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])).json()

    new_dictionary = {}
    new_dictionary['task'] = []
    for index in response:
        new_dictionary['task'].append({
            index.get('userId'), index.get('title'),
            index.get('completed'), name_of_employee.get('username')})

    with open("{}.json".format(argv[1]), 'w') as filename:
        json.dump(new_dictionary, filename)

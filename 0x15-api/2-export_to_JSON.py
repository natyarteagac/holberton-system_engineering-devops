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

    new_dictionary = {argv[1]: []}
    for num, task in enumerate(response):
        new_dictionary[argv[1]].append({
            'task': response[num].get('title'),
            'completed': response[num].get('completed'),
            'username': name_of_employee.get('username')})

    with open("{}.json".format(argv[1]), 'w') as filename:
        json.dump(new_dictionary, filename)

#!/usr/bin/python3
""" Export to CSV """

import csv
import json
import requests

if __name__ == '__main__':
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()
    name_of_employee = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()

    new_dictionary = {}
    for user in name_of_employee:
        new_list = []
        for all_dict in response:
            if user.get('id') == all_dict.get('userId'):
                new_list.append({
                    'task': all_dict.get('title'),
                    'completed': all_dict.get('completed'),
                    'username': user.get('username')})
                new_dictionary[user.get("id")] = new_list
    with open("todo_all_employees.json", 'w') as filename:
        json.dump(new_dictionary, filename)

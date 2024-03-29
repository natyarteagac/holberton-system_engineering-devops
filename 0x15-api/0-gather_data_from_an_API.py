#!/usr/bin/python3
""" Python request """

import requests
from sys import argv

if __name__ == '__main__':
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".
        format(argv[1])).json()
    name_of_employee = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])).json()
    counter = 0
    for index in response:
        if index.get('completed') is True:
            counter += 1
    print("Employee {} is done with tasks({}/{}): ".format(
        name_of_employee.get('name'), counter, len(response)))
    for index in response:
        if index.get('completed') is True:
            print("\t {}".format(index.get('title')))

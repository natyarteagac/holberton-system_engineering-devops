#!/usr/bin/python3
""" Export to CSV """

import csv
import requests
from sys import argv

if __name__ == '__main__':
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".
        format(argv[1])).json()
    name_of_employee = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])).json()

    with open("{}.csv".format(argv[1]), "w") as file_csv:
        f = csv.writer(file_csv, quoting=csv.QUOTE_ALL)
        list_append = []
        for index in response:
            list_append.append(index)
            f.writerow(
                [index.get('userId'), name_of_employee.get
                    ('name'), index.get('completed'), index.get('title')])

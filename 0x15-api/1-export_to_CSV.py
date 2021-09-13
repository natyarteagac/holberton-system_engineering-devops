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
        f = csv.writer(file_csv)
        f.writerow("response")
        f.writerow("name_of_employee")
        for index in response:
            f.writerows("{}, {}, {}, {}".
                        format(index.get('userId'),
                               name_of_employee.get('name'), index.get(
                            'completed'), index.get('title')))

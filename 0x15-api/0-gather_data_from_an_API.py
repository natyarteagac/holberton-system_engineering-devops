#!/usr/bin/python3
""" Python request """

from sys import argv
import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.json())

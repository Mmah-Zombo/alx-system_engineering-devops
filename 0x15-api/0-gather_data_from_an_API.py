#!/usr/bin/python3
"""returns information about his/her TODO list progress"""
import json
import requests
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(sys.argv[1]))
    todos = requests.get(url + "todos",
                         params={'userId': sys.argv[1]})

    tasks = 0
    for each in todos:
        tasks += 1

    completed_tasks = [x.get('title') for x in todos
                       if x.get('completed') is True]

    print("Employee {} is done with tasks({}/{}):"
          .format(employee['name'], len(completed_tasks), tasks))

    [print("\t {}".format(each)) for each in completed_tasks]

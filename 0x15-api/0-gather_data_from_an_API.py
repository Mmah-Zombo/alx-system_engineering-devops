#!/usr/bin/python3
"returns information about his/her TODO list progress"
import sys
import requests 

if __name__ == '__main__':
  employee = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])).json()
  todos = requests.get("https://jsonplaceholder.typicode.com/todos/{}".format(sys.argv[1])).json()
  

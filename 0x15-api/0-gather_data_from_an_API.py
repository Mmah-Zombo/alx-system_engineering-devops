#!/usr/bin/env python
#!/usr/bin/python3
"returns information about his/her TODO list progress"
import requests 
import sys

if __name__ == '__main__':
  employee = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])).json()
  todos = requests.get("https://jsonplaceholder.typicode.com/todos", params={'userId': employee['id'],}).json()
  tasks = len(todos)
  completed_tasks = [x['title'] for x in todos if x['completed'] == True]

  print("Employee {} is done with tasks({}/{}):".format(employee['name'], len(completed_tasks), tasks))

  for each in completed_tasks:
    print("\t {}".format(each))

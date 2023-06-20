#!/usr/bin/python3
"returns information about his/her TODO list progress"
import requests
import sys

def get_employee_todo_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve employee information for ID {employee_id}")
        return

    employee = response.json()
    employee_name = employee.get("name")

    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"userId": employee_id})
    if response.status_code != 200:
        print(f"Failed to retrieve TODO list for employee ID {employee_id}")
        return

    todos = response.json()
    completed_tasks = [todo for todo in todos if todo.get("completed")]

    total_tasks = len(todos)
    completed_count = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks ({completed_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide the employee ID as a parameter.")
    else:
        employee_id = sys.argv[1]
        get_employee_todo_progress(employee_id)

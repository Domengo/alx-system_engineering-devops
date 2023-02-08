#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
returns info about employee TODO progress
Implemented using recursion
"""
import requests
from sys import argv


def get_todo_list(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    response = requests.get(url)
    if response.status_code == 200:
        todo_list = response.json()
        done_tasks = [task for task in todo_list if task["completed"] is True]
        done_tasks_count = len(done_tasks)
        total_tasks_count = len(todo_list)
        name = todo_list[0]["userId"]
        employee_name = f"Employee {todo_list.get('name')}"
        print(f"{employee_name} is done with tasks\
              ({done_tasks_count}/{total_tasks_count}): ")

        for task in done_tasks:
            print(f"\t {task['title']}")
    else:
        print("An error has occurred while trying to retrieve the TODO list")


if __name__ == '__main__':
    employee_id = argv[1]
    get_todo_list(employee_id)

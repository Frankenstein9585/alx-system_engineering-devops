#!/usr/bin/python3
"""
This script uses a REST API for a given employee ID,
returns information about his/her TO-DO list progress.
"""
import csv
import json

import requests
import sys


def employee_todo_progress():
    """This function gets the employees to-do progress"""
    url = 'https://jsonplaceholder.typicode.com'

    # employee details
    employee_url = '{}/users/'.format(url)
    response = requests.get(employee_url)
    employee_data = response.json()
    # print(employee_data)

    # print(employee_data)
    # employee's to-do list
    todo_url = '{}/todos/'.format(url)
    response = requests.get(todo_url)
    todo_data = response.json()
    # print(todo_data)

    json_data = {}
    for employee in employee_data:
        task_list = []
        for task in todo_data:
            i = 0
            task_dict = task.copy()
            task_dict.pop('userId')
            task_dict.pop('id')
            task_dict['task'] = task_dict['title']
            del task_dict['title']
            task_dict['username'] = employee.get('username')
            task_list.append(task_dict)
        json_data[employee.get('id')] = task_list

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    # employee_id = sys.argv[1]
    employee_todo_progress()

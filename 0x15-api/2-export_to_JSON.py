#!/usr/bin/python3
"""
This script uses a REST API for a given employee ID,
returns information about his/her TO-DO list progress.
"""
import csv
import json

import requests
import sys


def employee_todo_progress(employee_id):
    """This function gets the employees to-do progress"""
    url = 'https://jsonplaceholder.typicode.com'

    # employee details
    employee_url = '{}/users/{}'.format(url, employee_id)
    response = requests.get(employee_url)
    employee_data = response.json()

    # print(employee_data)
    # employee's to-do list
    todo_url = '{}/todos/?userId={}'.format(url, employee_id)
    response = requests.get(todo_url)
    todo_data = response.json()

    task_list = []
    for task in todo_data:
        task_dict = task.copy()
        task_dict.pop('userId')
        task_dict.pop('id')
        task_dict['task'] = task_dict['title']
        del task_dict['title']
        task_dict['username'] = employee_data.get('username')
        task_list.append(task_dict)

    json_data = {employee_id: task_list}

    with open('{}.json'.format(employee_id), 'w', ) as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    employee_id = sys.argv[1]
    employee_todo_progress(employee_id)

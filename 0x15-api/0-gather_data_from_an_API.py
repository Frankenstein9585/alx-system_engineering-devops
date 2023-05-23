#!/usr/bin/python3
"""
This script uses a REST API for a given employee ID,
returns information about his/her TO-DO list progress.
"""

import requests
import sys


def employee_todo_progress(employee_id):
    """This function gets the employees to-do progress"""
    url = 'https://jsonplaceholder.typicode.com'

    # employee details
    employee_url = '{}/users/{}'.format(url, employee_id)
    response = requests.get(employee_url)
    employee_data = response.json()

    # employee's to-do list
    todo_url = '{}/todos/?userId={}'.format(url, employee_id)
    response = requests.get(todo_url)
    todo_data = response.json()

    # Get required info
    employee_name = employee_data.get('name')
    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task.get('title')]
    num_completed_tasks = len(completed_tasks)

    # Display progress
    print('Employee {} is done with tasks ({}/{}):'.format(
        employee_name, num_completed_tasks, total_tasks))
    for task in completed_tasks:
        print('\t', task.get('title'))


if __name__ == "__main__":
    employee_id = sys.argv[1]
    employee_todo_progress(employee_id)

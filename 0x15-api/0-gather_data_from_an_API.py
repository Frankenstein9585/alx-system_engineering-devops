#!/usr/bin/python3
import requests


def employee_todo_progress(employee_id):
    url = 'https://jsonplaceholder.typicode.com/'

    # employee details
    employee_url = '{}/users/{}'.format(url, employee_id)
    response = requests.get(employee_url)
    employee_data = response.json()

    # employee's to-do list
    todo_url = '{}/todos/{}'.format(url, employee_id)
    response = requests.get(todo_url)
    todo_data = response.json()

    # Get required info
    employee_name = employee_data['name']
    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task['completed']]
    num_completed_tasks = len(completed_tasks)

    # Display progress
    print('Employee {} is done with tasks ({}/{}):'.format(employee_name, num_completed_tasks, total_tasks))
    for task in completed_tasks:
        print('\t', task['title'])


employee_id = int(input())
employee_todo_progress(employee_id)

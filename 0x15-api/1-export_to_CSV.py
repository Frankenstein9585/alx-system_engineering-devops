#!/usr/bin/python3
"""
This script uses a REST API for a given employee ID,
returns information about his/her TO-DO list progress.
"""
import csv

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
    # print(todo_data)

    # Get required info
    employee_name = employee_data.get('name')
    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task.get('completed')]
    num_completed_tasks = len(completed_tasks)

    with open('{}.csv'.format(employee_id), 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        for task in todo_data:
            csv_list = [employee_id, employee_data.get("username"),
                        task.get('completed'), task.get('title')]
            formatted_list = ['"{}"'.format(item) for item in csv_list]
            print(formatted_list)

            csv_writer.writerow(formatted_list)


if __name__ == "__main__":
    # employee_id = sys.argv[1]
    employee_todo_progress(2)

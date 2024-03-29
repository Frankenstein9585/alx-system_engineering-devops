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

    with open('{}.csv'.format(employee_id), 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        for task in todo_data:
            csv_list = [employee_id, employee_data.get("username"),
                        task.get('completed'), task.get('title')]

            csv_writer.writerow(csv_list)


if __name__ == "__main__":
    employee_id = sys.argv[1]
    employee_todo_progress(employee_id)

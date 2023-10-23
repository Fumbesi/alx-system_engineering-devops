#!/usr/bin/python3
"""
Python script to gather employee TODO list progress from a REST API.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    # Define the API endpoint and the employee's tasks endpoint
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    # Fetch employee data and TODO list
    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        user_data = user_response.json()
        todos_data = todos_response.json()

        if (user_response.status_code != 200 or
                todos_response.status_code != 200):
            print("Employee not found")
        else: 
            employee_name = user_data["name"]
            total_tasks = len(todos_data)
            completed_tasks = [task for task in todos_data 
        if task["completed"]]
            num_completed_tasks = len(completed_tasks)

            print("Employee {} is done with tasks({}/{}):".format(
                employee_name, num_completed_tasks, total_tasks))
            for task in completed_tasks:
                print("\t {}".format(task["title"]))
    except Exception as e:
        print("An error occurred:", e)

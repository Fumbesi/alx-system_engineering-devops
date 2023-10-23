#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""


import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 1:
        sys.exit()

    # Define the URL of the API
    url = "https://jsonplaceholder.typicode.com/todos"

    # Send a GET request to the API
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the JSON response
        tasks = response.json()

        # Create a dictionary to store tasks by user ID
        tasks_by_user = {}

        for task in tasks:
            user_id = task["userId"]
            task_data = {
                "username": "",  # You can fetch the username from another endpoint
                "task": task["title"],
                "completed": task["completed"],
            }

            # Add the task to the corresponding user's list of tasks
            if user_id in tasks_by_user:
                tasks_by_user[user_id].append(task_data)
            else:
                tasks_by_user[user_id] = [task_data]

        # Save the tasks to a JSON file
        with open("todo_all_employees.json", "w") as json_file:
            json.dump(tasks_by_user, json_file, indent=4)
    else:
        print("Request failed with status code:", response.status_code)

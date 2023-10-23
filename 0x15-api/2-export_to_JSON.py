#!/usr/bin/python3
"""
Python script to gather list progress from a REST API and export it to a JSON file.
"""

import json
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

        if user_response.status_code != 200 
        or todos_response.status_code != 200:
            print("Employee not found")
        else:
            user_data = user_response.json()
            todos_data = todos_response.json()
            employee_name = user_data["username"]
            json_filename = "{}.json".format(employee_id)

            # Create a dictionary in the required format
            data_dict = {employee_id: []}
            for task in todos_data:
                data_dict[employee_id].append({
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": employee_name
                })

            # Write the data to a JSON file
            with open(json_filename, "w") as json_file:
                json.dump(data_dict, json_file, indent=4)

            print("Data exported to {}.".format(json_filename))

    except Exception as e:
        print("An error occurred:", e)


#!/usr/bin/python3
"""
Python script to export employee TODO list progress to a CSV file.
"""

import csv
import requests
import sys

if __name__ == "__main":
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
            employee_name = user_data["username"]
            csv_filename = "{}.csv".format(employee_id)

            with open(csv_filename, mode='w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

                for task in todos_data:
                    csv_writer.writerow([employee_id, employee_name, task["completed"], task["title"]])

            print("Data exported to {}.".format(csv_filename))
    except Exception as e:
        print("An error occurred:", e)

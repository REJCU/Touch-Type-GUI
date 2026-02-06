"""
Takes results of touch typing session and saves it to a json file.
"""

import json 
import datetime

attempt_date = datetime.datetime.now()

class RecordResults():
    def __init__(self):
        super().__init__()

    def print_to_json(self, data):
        # Sends to the json file. 
        with open("results.json", "a") as f:
            date =  f"{attempt_date.day}-{attempt_date.month}-{attempt_date.year}"
            # Init the new assignment
            data["Date"] = date
            data = json.dumps(data)
            print(data)
            print(type(data))
            print(date)
            f.write(data + "\n")





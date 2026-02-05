"""
Takes results of touch typing session and saves it to a json file.
"""

import json 

class RecordResults():
    def __init__(self):
        super().__init__()

    def print_to_json(self, data):
        # Sends to the json file. 
        with open("results.json", "a") as f:
            data = json.dumps(data)
            print(data)
            f.write(data)





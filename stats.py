import json 

class RecordResults():
    def __init__(self):
        super().__init__()

    def convert_to_json(self, text):
        print("convert_to_json",text)
        print(type(text))
        json_text = json.loads(text)
        print(json_text["Time"])



    def print_to_json(self):
        pass



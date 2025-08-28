import json
from idlelib import testing

data = {"name": "Jared", "age": 30}
# json_string = json.dumps(data)
# print(json_string)

open("data.json", "w").close()

testing = False
if testing:
    with open("data.json", "w") as f:
        json.dump(data, f)
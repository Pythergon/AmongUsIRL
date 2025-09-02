import json

def readData(filename="gamestate.json"):
    """Reads and returns data from a JSON file."""
    with open(filename, "r") as f:
        return json.load(f)

def completeTask(data, player_name, task_name):
    """Finds and sets a specific task to done."""
    for player in data['players']:
        if player['player_name'] == player_name:
            for task in player['taskList']:
                if task['task_name'] == task_name:
                    task['isDone'] = True
                    return True  # Task found and updated
    return False  # Task not found

def writeData(data, filename="gamestate.json"):
    """Writes the updated data back to the JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

JSONdata = readData()
task_completed = completeTask(JSONdata, "Jared", "Wires")
writeData(JSONdata)

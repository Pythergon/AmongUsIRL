import json

def read_data(filename="data.json"):
    """Reads and returns data from a JSON file."""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Handle case where file doesn't exist or is empty/invalid
        return []

def find_and_complete_task(data, player_name, task_name):
    """Finds and sets a specific task to done."""
    for player in data:
        if player['player_name'] == player_name:
            for task in player['taskList']:
                if task['task_name'] == task_name:
                    task['isDone'] = True
                    return True  # Task found and updated
    return False  # Task not found

def write_data(data, filename="data.json"):
    """Writes the updated data back to the JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

player_data = read_data()
task_completed = find_and_complete_task(player_data, "Jared", "Wires")

if task_completed:
    print("Task 'Wires' for Jared has been marked as complete.")
    write_data(player_data)
else:
    print("Task not found.")
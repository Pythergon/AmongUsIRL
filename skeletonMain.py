# Main.py without socketing
# Made for testing without too many varibles!
import json
import time

listOfTasks = []
class Task:
    def __init__(self, name, location):
        self.isDone = False
        self.name = name
        self.location = location
        self.isAssigned = False # Not sure if needed but might be nice later
        listOfTasks.append(self)

    def finishTask(self):
        self.isDone = True

    def toString(self):
        print(f"{self.name} - Task is done: ({self.isDone}) - Task location: {self.location}")

    def toJSON(self):
        return {"isDone": self.isDone, "task_name": self.name, "location": self.location}

class Player:
    def __init__(self, name):
        self.name = name
        self.taskList = []
        self.isDead = False
        self.JSONtaskList = []

    def __getitem__(self, item):
        return self.taskList[item]

    def toJSON(self):
        return {"player_name": self.name, "isDead": self.isDead, "taskList": self.JSONtaskList}

    def addTaskToList(self, task):
        if isinstance(task, Task):
            self.taskList.append(task)
            self.JSONtaskList.append(task.toJSON())
            task.isAssigned = True
        else:
            print(f"{str(task)} is not the required type!")
            pass

# Tests:
player1 = Player("Jared")
player2 = Player("Owen")
task1 = Task("Wires", "Kitchen")
task2 = Task("Medbay Scan", "Living Room")
task3 = Task("Swipe Card", "Boys Room")
task4 = Task("Prime Sheilds", "Front Room")
task5 = Task("Clear Astroids", "Mudroom")

# task1.toString()
player1.addTaskToList(task1)
player1.addTaskToList(task2)
player2.addTaskToList(task3)

finalFormat = [player1.toJSON(), player2.toJSON()]

with open("data.json", "w") as json_file:
    json.dump(finalFormat, json_file, indent=4)

# Now i need to make a game loop to always set the task and player info as it is in the JSON file
# Things needed to change - isDone Status and isDead Status
running = True
while running:
    with open("data.json", "r") as json_file:
        # Use json.load() to read the JSON data from the file
        loaded_data = json.load(json_file)

    time.sleep(1)
    for player in loaded_data:
        print(f"Tasks for {player['player_name']}:")
        for task in player['taskList']:
            print(f"  - Task Name: {task['task_name']}, Location: {task['location']}, Done: {task['isDone']}")
            if task['isDone']:
                running = False
                print("What?")


    # running = True # Stop after 1 iteration!

# Main.py without socketing
# Made for testing without too many varibles!
import json
import time

class Game:
    def __init__(self, debugMode):
        self.debugMode = debugMode
        self.players = []
        self.playersJSON = []
        self.tasks = []
        self.tasksJSON = []
        self.running = True

    def addPlayerToList(self, player):
        if isinstance(player, Player):
            self.players.append(player)
            self.playersJSON.append(player.toJSON())
        else:
            print("Expect player object as input")
            pass

    def addTaskToList(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)
            self.tasksJSON.append(task.toJSON())
        else:
            print("Expected task object as input")
            pass

    def toJSON(self):
        return {"players": self.playersJSON, "tasks": self.tasksJSON}

listOfTasks = []
class Task:
    def __init__(self, name, location):
        self.isDone = False
        self.name = name
        self.location = location
        self.isAssigned = False # Not sure if needed but might be nice later
        listOfTasks.append(self)

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

"""Object decleration"""
game = Game(False)
# player1 = Player("Jared")
# player2 = Player("Owen")
task1 = Task("Wires", "Kitchen")
task2 = Task("Medbay Scan", "Living Room")
task3 = Task("Swipe Card", "Boys Room")
task4 = Task("Prime Sheilds", "Front Room")
task5 = Task("Clear Astroids", "Mudroom")
# game.addPlayerToList(player1)
# game.addPlayerToList(player2)
game.addTaskToList(task1)
game.addTaskToList(task2)
game.addTaskToList(task3)
game.addTaskToList(task4)
game.addTaskToList(task5)

# task1.toString()
# player1.addTaskToList(task1)
# player1.addTaskToList(task2)
# player2.addTaskToList(task3)

with open("gamestate.json", "w") as json_file:
    json.dump(game.toJSON(), json_file, indent=4)

# Now i need to make a game loop to always set the task and player info as it is in the JSON file
# Things needed to change - isDone Status and isDead Status

while game.running:
    with open("gamestate.json", "r") as json_file:
        # Use json.load() to read the JSON data from the file
        loaded_data = json.load(json_file)

    time.sleep(1)
    if game.debugMode:
        for player in loaded_data['players']:
            print(f"Tasks for {player['player_name']}")
            for task in player['taskList']:
                print(f"  - Task Name: {task['task_name']}, Location: {task['location']}, Done: {task['isDone']}")
                if task['isDone']:
                    game.running = False


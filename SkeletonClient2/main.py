import os
import json

class Client:
    def __init__(self, name):
        self.path = os.getcwd()
        self.JSONpath = f"{self.path}/clientJSON.json"
        self.UUID = "6b8d9c22-7f15-4e3a-b8d4-5a6f2c3e1b7a"
        self.name = name
        self.taskList = []
        self.isDead = False
        self.JSONtaskList = []

    def __getitem__(self, item):
        return self.taskList[item]

    def toJSON(self):
        return {"Path": self.JSONpath, "UUID": self.UUID,"player_name": self.name, "isDead": self.isDead, "taskList": self.JSONtaskList}

# Need to initiate client!
# I don't have internet so lets do this later

player = Client("Jared")
print(player.path)
print(player.JSONpath)

with open(player.JSONpath, 'w') as f:
    json.dump(player.toJSON(), f, indent=4)



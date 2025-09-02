import json

class Game:
    def __init__(self, debugMode):
        self.debugMode = debugMode
        self.running = True

    def toJSON(self):
        return {}

    def getClientJSON(self):
        with open(r"C:\Users\jared\AmongUsIRL\SkeletonClient2/clientJSON.json", "r") as json_file:
            # Use json.load() to read the JSON data from the file
            loaded_data = json.load(json_file)
        return loaded_data

game = Game(True)
print(game.getClientJSON())

while game.running:
    break

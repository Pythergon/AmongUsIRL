import json

class Game:
    def __init__(self, debugMode):
        self.debugMode = debugMode
        self.running = True

    def toJSON(self):
        return {}

game = Game(True)

while game.running:


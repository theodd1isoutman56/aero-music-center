import json
import os
class playlist1:
    def __init__(self, filename="playlist.json"):
        self.filename = filename
    def save(self, playlist):
        with open(self.filename, "w", encoding ="utf-8") as file:
            json.dump(playlist, file, indent= 4)
    def load(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r', encoding = "utf-8") as file:
            return json.load(file)
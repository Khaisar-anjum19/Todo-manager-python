import json
import os
class Storage:
    FILE_NAME = "tasks.json"

    @staticmethod
    def load_tasks():
        if not os.path.exists(Storage.FILE_NAME):
            return []
        with open(Storage.FILE_NAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []

    @staticmethod
    def save_tasks(tasks):
        with open(Storage.FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)
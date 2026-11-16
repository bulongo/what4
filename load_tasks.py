import json
def load_tasks():
    try:
        with open("tasks.json","r",encoding="utf-8") as f:
            return json.load(f)
    except(FileNotFoundError, json.JSONDecodeError):
        return[]


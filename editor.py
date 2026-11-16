import json
from show_tasks import show_tasks
from load_tasks import load_tasks

def editor(Tasks):
        print("") 
        print("You are now in EDIT mode.")
        show_tasks(Tasks)
        all_tasks = load_tasks()
        task_number = int(input("Select task(by number) that you would like to edit: "))
        print(all_tasks[task_number - 1])
        new_task = input("What would you like to change it to?: ")
        all_tasks[task_number - 1]["body"] = new_task
        with open("tasks.json", "w", encoding="utf-8") as f:
            json.dump(all_tasks,f,indent=4)
        print(f"Your new tasks are now {all_tasks}")



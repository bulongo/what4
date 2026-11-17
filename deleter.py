import json
from show_tasks import show_tasks
from load_tasks import load_tasks


def deleter(Tasks):
    print("You are in DELETE mode")
    show_tasks(Tasks)
    all_tasks = load_tasks()
    task_number = int(input("Select task(by number) that you would like to delete: "))
    all_tasks.remove(all_tasks[task_number - 1])
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(all_tasks,f,indent=4)
    print(f"Your new tasks are now {all_tasks}")



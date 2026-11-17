import json
from dataclasses import asdict
from load_tasks import load_tasks
from classes.Task import Task
from functions.clear import clear
from functions.exiter import exiter

def adder(Tasks):
    # task_title = input("Add task category: ")
    task_body = input("Task: ")
    new_task = Task(task_body)
    Tasks.append(new_task)
    clear()

    def choice_func():
        choice = input("would you like to add more tasks (y/n): ")
        if(choice == "y"):
            adder(Tasks)
        elif(choice == "n"):
            save_and_exit = input("would you like to save and exit(y) or just exit(n)?: ")
            if(save_and_exit == 'y'):
                data = [{**asdict(t)} for t in Tasks]
                # saved_tasks.append(data)
                saved_tasks = load_tasks()
                for i in range(len(data)):
                    if(data == []):
                        print("There is nothing to add")
                    else:
                        saved_tasks.append(data[i])
                        with open("tasks.json","w",encoding="utf-8") as g:
                            json.dump(saved_tasks,g, indent=4)
                exiter()
                exit()
            else:
                exit()
        else:
            print("Invalid option. please choose between 'y' and 'n': ")
            choice_func()
    
    choice_func()


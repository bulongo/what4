################## WHAT4 #################

import json
import time
from pathlib import Path
import os
from dataclasses import dataclass, asdict

print("WHAT4")

def clear():
    os.system("clear")

# if(Path("tasks.json").exists()):
#     with open("tasks.json", "w", enconding="utf-8") as file:
#     pass
# else:
#     print("File does not exist")
#
print("** TO STOP ADDING TASKS, TYPE 'done' AND PRESS ENTER **")
print()
time.sleep(1)
running = True
Tasks = []

@dataclass
class Task:
    # category: str
    body: str
    completed: bool = False
    
    def say_task(self):
        return f"{self.body}"


def exiting_text():
        clear()
        print("Saving file and exiting")
        time.sleep(.3)
        clear()
        print("Saving file and exiting.")
        time.sleep(.3)
        clear()
        print("Saving file and exiting..")
        time.sleep(.3)
        clear()
        print("Saving file and exiting...")
        time.sleep(1)
        exit()


def choices():
        action = input("Would you like to (E)dit,(D)elete,e(X)it?: ")
        if(action == "E" or action == "e"):
            editor()
        elif(action == "D" or action == "d"):
            deleter()
        elif(action == "X" or action == "x"):
            exiting_text()

def adder():
    # task_title = input("Add task category: ")
    task_body = input("Task: ")
    new_task = Task(task_body)
    Tasks.append(new_task)
    clear()

    print("")
    print("##############################")
    print("")
    print("---- CURRENT TASKS ----")
    print("")
    for task in Tasks:
        print(f"- {task}")
    print("")
    print("##############################")


    choice = input("would you like to add more tasks (y/n): ")

    if(choice == "y"):
        adder()
    elif(choice == "n"):
        save_and_exit = input("would you like to save and exit(y) or just exit(n)?: ")
        if(save_and_exit == 'y'):
            data = [{**asdict(t)} for t in Tasks]
            with open("tasks.json","w") as f:
                json.dump(data,f, indent=4)
            exit()
        else:
            exit()
        # choices()
    else:
        choice = input("Invalid option. please choose between 'y' and 'n': ")


def editor():
        print("You are now in edit mode.")
        print("Select a task you would like to edit.")
        if(Tasks != []):
            for task in Tasks:
                print(task)
        else:
            print("No tasks to edit.")


def deleter():
    print("We will clean house")

def show_tasks():
    if(Tasks == []):
        print("You have no tasks in your tasks list.")
        ans = input("Would you like to add tasks?(y/n): ")
        if(ans == "y"):
            adder()
        elif(ans == "n"):
            choices()
        else:
            ans = input("invalid choice, please try again: ")
        
    else:
        print(Tasks)

show_tasks()

# while(running):
#     # if((action == "e" or action == "E") and tasks != []):
#     #     editor()
#     if(task == "done"):
#         print("Saving to file and ending programme")
#         running = False
#     if(task == ""):
#         print("You can't add an empyty task")
#         task = input("Task?: ")
#     else:
#         tasks.append(task)
#         print("Task added!")
#         print("Tasks = %s" %tasks)
#


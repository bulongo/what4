import time
from pathlib import Path
import os
from dataclasses import dataclass

print("WHAT4")

def clear():
    os.system("clear")

if(Path("tasks.json").exists()):
    # with open("tasks.txt", "w", enconding="utf-8") as file:
    pass
else:
    print("File does not exist")

print("** TO STOP ADDING TASKS, TYPE 'done' AND PRESS ENTER **")
print()
time.sleep(1)
running = True
tasks = []

@dataclass
class Task:
    title: str
    body: str
    completed: bool = False
    
    def say_title(self):
        return f"{self.title}"


def exiting_text():
        clear()
        print("Saving file and exiting")
        time.sleep(1)
        clear()
        print("Saving file and exiting.")
        time.sleep(1)
        clear()
        print("Saving file and exiting..")
        time.sleep(1)
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
    task_title = input("Add task title: ")
    task_body = input("Task: ")
    new_task = Task(task_title,task_body)
    tasks.append(new_task)
    # print(tasks[0].title)
    choice = input("would you like to add more tasks (y/n): ")
    if(choice == "y"):
        adder()
    elif(choice == "n"):
        save_and_exit = input("would you like to save and exit(y) or just exit(n)?: ")
        if(save_and_exit == 'y'):
            with open("tasks.json","w") as f:
                json.dump(tasks,f, indent=4)
        else:
            exit()
        # choices()
    else:
        choice = input("invalid option. please choose beteween 'y' and 'n'")


def editor():
        print("You are now in edit mode.")
        print("Select a task you would like to edit.")
        if(tasks != []):
            for task in tasks:
                print(task)
        else:
            print("No tasks to edit.")


def deleter():
    print("We will clean house")


if(tasks == []):
    print("You have no tasks in your tasks list.")
    ans = input("Would you like to add tasks?(y/n): ")
    if(ans == "y"):
        adder()
    elif(ans == "n"):
        choices()
    else:
        ans = input("invalid choice, please try again: ")
    


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


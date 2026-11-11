import time
from pathlib import Path

print("WHAT4")

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

def choices():
        action = input("Would you like to (E)dit,(D)elete,e(X)it?: ")
        if(action == "E" or action == "e"):
            editor()
        elif(action == "D" or action == "d"):
            deleter()
        elif(action == "X" or action == "x"):
            print("Saving file and exiting")
            time.sleep(3)
            exit()



def editor():
        print("You are now in edit mode.")
        print("Select a task you would like to edit.")
        for task in tasks:
            print(task)


def adder():
    task = input("Add task: ")
    tasks.append(task)
    print(tasks)
    choice = input("would you like to add more tasks (y/n): ")

    if(choice == "y"):
        adder()
    else:
        choices()


def deleter():
    print("We will clean house")


if(tasks == []):
    print("You have no tasks in your tasks list.")
    ans = input("Would you like to add tasks?(y/n): ")
    if(ans == "y"):
        adder()
    elif(ans == "n"):
        choices()
    


while(running):
    # if((action == "e" or action == "E") and tasks != []):
    #     editor()
    task = input("What task would you like to complete today?: ")
    if(task == "done"):
        print("Saving to file and ending programme")
        running = False
    if(task == ""):
        print("You can't add an empyty task")
        task = input("Task?: ")
    else:
        tasks.append(task)
        print("Task added!")
        print("Tasks = %s" %tasks)



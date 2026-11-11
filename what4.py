import time
import pathlib

print("WHAT4")

name = input("Please enter your name here: ")
print("Hello there %s" %name)
print()
print("** TO STOP ADDING TASKS, TYPE 'done' AND PRESS ENTER **")
print()
time.sleep(1)
running = True
tasks = []

action = input("Would you like to (E)dit,(D)elete,(A)dd a task?: ")

def editor():
        print("You are now in edit mode.")
        print("Select a task you would like to edit.")
        for task in tasks:
            print(task)

def adder():
    print("something for the people-dem")

def deleter():
    print("We will clean house")


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



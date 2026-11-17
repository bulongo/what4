from adder import adder
from editor import editor
from deleter import deleter
from functions.exiter import exiter


def action_selector(Tasks):
        action = input("Would you like to (A)dd a task, (E)dit,(D)elete or e(X)it?: ")
        if(action == "A" or action =="a"):
            adder(Tasks)
        elif(action == "E" or action == "e"):
            editor(Tasks)
        elif(action == "D" or action == "d"):
            deleter(Tasks)
        elif(action == "X" or action == "x"):
            exiter()


from load_tasks import load_tasks
from adder import adder


def show_tasks(Tasks):
    saved_tasks = load_tasks()

    if(saved_tasks == []):
        print("You have no tasks in your tasks list.")
        ans = input("Would you like to add tasks?(y/n): ")
        if(ans == "y"):
            adder(Tasks)
        elif(ans == "n"):
            from action_selector import action_selector
            action_selector(Tasks)
        else:
            ans = input("invalid choice, please try again: ")
    else:
        print("##############################")
        print("")
        if(len(Tasks) > 1):
            print(f"---- YOU CURRENTLY HAVE {len(Tasks)} TASKS ----")
        elif(len(Tasks) == 1):
            print(f"---- YOU CURRENTLY HAVE {len(Tasks)} TASKS ----")
        print("")
        for task in saved_tasks:
            print(f"- {task["body"]}")
            if(task["completed"] == False):
                print(f"    state: pending")
            else:
                print(f"    state: complete")
            print("")
        print("##############################")
        print("")


# Big idea -> Custom Commands -> Run using manual syntax (not the best thing but it gets the job done)

errors = {
    "404": "{Program-Name} not found.",
    "403": "{Program-Name} has blocked Task Manager from accessing it.",
    "1": "Runtime error occured. Task Manager lasted {taskmanager-runtime} without crashing.",
    "2": "There are no tasks. Please come back when you add a task.",
    "3": "Task time wasn't scheduled.",
    "4": "Cannot create file in my own content folder please report this issue immediately.",
    "5": "Logs file wasn't found",
    "6": "Tasks file wasn't found",
    "7": "Program needs to update. Check https://github.com/liablelua/Task-Manager/",
    "8": "Invalid task syntax"
}

version = "c4ca4238a0b923820dcc509a6f75849b"
ghVersion =  "c4ca4238a0b923820dcc509a6f75849b" # change to get request soon?

def run_task(task):
    splitFirstTask = split(task[0], " ")
    isEnabled = FALSE

    try: 
        if splitFirstTask[0] == "@TASKMANAGER" && splitFirstTask[1] == "ENABLE" && splitFirstTask[2] == NULL:
            
        else:
            exit() # Change to message box later
    except:
        exit() # Change to message box later


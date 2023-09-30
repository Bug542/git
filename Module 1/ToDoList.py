tasks = []

def add_task(task):
    
  ## Add a new task to the to-do list
    tasks.append(task)
    print(f"Added task:{task}")
  
def remove_task(task):

  ## If else statement for removinh tasks
  ## this will also print a "remove task"

    if task in tasks:
        tasks.remove(task)
        print(f"Remove task: {task}")
    else:
        print(f"{task} not found")
    
def view_task():

    ## view all tasks in list
    ## pritn statemnt to vie taks that have been stored

    print("To-do List:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

    ## Display the options base on id for user to pick
      
while True:
    print ("\nwhat do you want to do")
    print ("1. ADD a Task" )
    print ("2. Remove a task")
    print ("3. View all task")
    print ("4. Exit")

    ## if else statemnt for id 
    ## This wil provide option to add,remove,view, and exit task

    choice = input("Enter choice")

    if choice == "1":
        task = input("Enter a new Task")
        add_task(task)
    elif choice == "2":
        task = input("Enter a new task")
        remove_task(task)
    elif choice == "3":
        view_task()
    elif choice == "4":
        print("Exit")
        break
    else:
            print("Invalid Choice !")
def addTask(taskList, task):
    taskList.append(task)
    print(f"Task '{task}' added to the list.")

def removeTask(taskList, task):
    if task in taskList:
        taskList.remove(task)
        print(f"Task '{task}' removed from the list.")
    else:
        print(f"Task '{task}' not found in the list.")

def displayTasks(taskList):
    if not taskList:
        print("No tasks in the list.")
    else:
        print("Tasks in the list:")
        for index, task in enumerate(taskList, start=1):
            print(f"{index}. {task}")

def saveTasks(taskList, filename):
    with open(filename, 'w') as file:
        '''
        for index, task in enumerate(taskList, start=1):
            file.write(f"{index}. {task}\n")
        '''
        for task in taskList:
            file.write(f"{task}\n")
    print(f"Tasks saved to '{filename}'.")

def loadTasks(filename):
    taskList = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                '''
                task = line.strip().split('. ', 1)[1]  # Extract task after the number and dot
                '''
                task = line.strip()  # strip newline characters
                taskList.append(task)
        print(f"Tasks loaded from '{filename}'.")
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with an empty task list.")
    return taskList

def main():
    taskList = []
    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Save Tasks")
        print("5. Load Tasks")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            task = input("Enter the task to add: ")
            addTask(taskList, task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            removeTask(taskList, task)
        elif choice == '3':
            displayTasks(taskList)
        elif choice == '4':
            filename = input("Enter the filename to save tasks: ")
            saveTasks(taskList, filename)
        elif choice == '5':
            filename = input("Enter the filename to load tasks: ")
            taskList = loadTasks(filename)
        elif choice == '6':
            print("Exiting the Todo List application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")



if __name__ == "__main__":
    main()
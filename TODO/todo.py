tasks = []

while True:
    print("\nTo-Do List App")
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == '2':
        task = input("Enter the task need to be removed: ")
        if task in tasks:
            tasks.remove(task)
            print("Task removed!")
        else:
            print("Task not found!")
    elif choice == '3':
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == '4':
        print("Exiting now..")
        break
    else:
        print("Invalid choice..!!Try again.")

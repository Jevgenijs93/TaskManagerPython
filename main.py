tasks = []

while True:
    print("\nMenu:")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        if len(tasks) == 0:
            print("Task list is empty")
        else:
            print("Task list:")
            for index, task in enumerate(tasks, start=1):
                print(index, "-", task)

    elif choice == "2":
         new_task = input("Enter new task: ")
         tasks.append(new_task)
         print("Task added")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice")

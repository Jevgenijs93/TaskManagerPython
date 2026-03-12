tasks = []

while True:
    print("\nMenu:")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        if len(tasks) == 0:
            print("Task list is empty")
        else:
            print("Task list:")
            for index, task in enumerate(tasks, start=1):
                status = "✓" if task["done"] else "✗"
                print(f"{index}. {task['title']} [{status}]")

    elif choice == "2":
         title = input("Enter new task: ")
         tasks.append({"title" : title, "done" : False})
         print("Task added")

    elif choice == "3":
        if len(tasks) == 0:
            print("We don't have any tasks to mark")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['title']}")

            num = int(input("Enter task number: "))
            if 1 <= num <= len(tasks):
                tasks[num-1]["done"] = True
                print("Task marked successfully as completed")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")

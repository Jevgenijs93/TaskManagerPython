def save_tasks(tasks):
    with open("tasks.txt", "w", encoding="utf-8") as file:
         for task in tasks:
             file.write(f"{task['title']}|{task['done']}\n")

def load_tasks():
    tasks = []
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            for line in file:
                title, done = line.strip().strip("|")
                tasks.append({
                    "title" : title,
                    "done" : done == "True"
                })
    except FileNotFoundError:
        print("Error: File not found")
        pass
    return tasks

tasks = load_tasks()

while True:
    print("\nMenu:")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

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
         save_tasks(tasks)
         print("Task added")

    elif choice == "3":
        if len(tasks) == 0:
            print("We don't have any tasks to mark")
        else:
            print("Task list:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['title']}")
        try:
            num = int(input("Enter task number: "))
            if 1 <= num <= len(tasks):
                tasks[num-1]["done"] = True
                save_tasks(tasks)
                print("Task marked successfully as completed")
            else:
                print("Task with that number does not exist")
        except ValueError:
            print("Error: Please enter number")

    elif choice == "4":
        if len(tasks) == 0:
            print("We don't have any tasks to delete")
        else:
            print("Task list:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['title']}")

        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                deleted_task = tasks.pop(num-1)
                save_tasks(tasks)
                print(f"Task '{deleted_task['title']}' deleted")
            else:
                print("Task with that number does not exist")

        except ValueError:
            print("Error: Please enter number")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")

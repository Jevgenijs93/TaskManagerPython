from asyncio import tasks
from pathlib import Path

TASKS_FILE = Path("tasks.txt")


def save_tasks(tasks, file_path=TASKS_FILE):
    with open(file_path, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(f"{task['title']}|{task['done']}\n")


def load_tasks(file_path=TASKS_FILE):
    tasks = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                title, done = line.strip().split("|")
                tasks.append({
                    "title": title,
                    "done": done == "True"
                })
    except FileNotFoundError:
        pass
    return tasks


def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)


def complete_task(tasks, index):
    if not tasks:
        print("Task list is empty")
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        return True
    return False


def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        return tasks.pop(index)
    return None


def show_tasks(tasks):
    if not tasks:
        print("Task list is empty")
        return
    print("Task list:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "✗"
        print(f"{index}. {task['title']} [{status}]")


def main():
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
            show_tasks(tasks)

        elif choice == "2":
            title = input("Enter new task title: ")
            add_task(tasks, title)
            save_tasks(tasks)
            print("Tasks added")

        elif choice == "3":
            if not tasks:
                print("We don't have any tasks to mark")
            else:
                show_tasks(tasks)
                try:
                    num = int(input("Enter task number: "))
                    if complete_task(tasks, num - 1):
                        show_tasks(tasks)
                        print("Task marked successfully as completed")
                    else:
                        print("Task with that number does not exist")
                except ValueError:
                    print("Error: Please enter number")

        elif choice == "4":
            if not tasks:
                print("We don't have any tasks to delete")
            else:
                show_tasks(tasks)
                try:
                    num = int(input("Enter task number to delete: "))
                    deleted_task = delete_task(tasks, num - 1)
                    if delete_task:
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


if __name__ == "__main__":
    main()

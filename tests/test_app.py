from pathlib import Path

# File where all tasks will be saved
TASKS_FILE = Path("tasks.txt")

# Save all tasks to a text file.
# Each task is saved in this format: title|done
def save_tasks(tasks, file_path=TASKS_FILE):

    with open(file_path, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(f"{task['title']}|{task['done']}\n")

# Load tasks from the text file.
# If the file does not exist, return an empty list.
def load_tasks(file_path=TASKS_FILE):
    tasks = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                # Remove newline characters and split the line into title and done status
                title, done = line.strip().split("|")

                # Convert the text value "True" or "False" back to a boolean
                tasks.append({
                    "title": title,
                    "done": done == "True"
                })

    except FileNotFoundError:
        # If the file does not exist yet, just return an empty task list
        pass

    return tasks

# Add a new task to the task list.
# New tasks are always marked as not completed.
def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)

# Mark a task as completed by its index.
# Returns True if the task was found and updated.
#  Returns False if the index is invalid.
def complete_task(tasks, index):
    if not tasks:
        print("Task list is empty")

    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        return True

    return False

# Delete a task by its index.
# Returns the deleted task if the index is valid.
# Returns None if the index is invalid.
def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        return tasks.pop(index)

    return None

# Display all tasks in the console.
# Completed tasks are shown with a check mark.
# Incomplete tasks are shown with a cross mark.
def show_tasks(tasks):

    if not tasks:
        print("Task list is empty")
        return

    print("Task list:")

    # start=1 makes task numbers more user-friendly
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "✗"
        print(f"{index}. {task['title']} [{status}]")

# Main program loop.
# Loads tasks from the file, shows the menu, and handles the user's choices.
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
            # Show all saved tasks
            show_tasks(tasks)

        elif choice == "2":
            # Ask the user for a new task title and add it to the list
            title = input("Enter new task title: ")
            add_task(tasks, title)
            print("Task added")

        elif choice == "3":
            # Mark an existing task as completed
            if not tasks:
                print("We don't have any tasks to mark")
            else:
                show_tasks(tasks)

                try:
                    # User sees task numbers starting from 1,
                    # but list indexes start from 0, so we subtract 1
                    num = int(input("Enter task number: "))

                    if complete_task(tasks, num - 1):
                        save_tasks(tasks)
                        show_tasks(tasks)
                        print("Task marked successfully as completed")
                    else:
                        print("Task with that number does not exist")

                except ValueError:
                    # This happens if the user enters text instead of a number
                    print("Error: Please enter number")

        elif choice == "4":
            # Delete an existing task
            if not tasks:
                print("We don't have any tasks to delete")
            else:
                show_tasks(tasks)

                try:
                    # Convert the user's task number to a list index
                    num = int(input("Enter task number to delete: "))
                    deleted_task = delete_task(tasks, num - 1)

                    if deleted_task:
                        save_tasks(tasks)
                        print(f"Task '{deleted_task['title']}' deleted")
                    else:
                        print("Task with that number does not exist")

                except ValueError:
                    # This happens if the user enters text instead of a number
                    print("Error: Please enter number")

        elif choice == "5":
            # Stop the program
            print("Exiting...")
            break

        else:
            # Handle menu options that do not exist
            print("Invalid choice")


# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()
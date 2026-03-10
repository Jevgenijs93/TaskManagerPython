tasks = []

while True:
    print("Menu:")
    print("1. Show tasks:")
    print("2. Add task:")
    print("3. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        if len(tasks) == 0:
            print("Task list is empty")
        else:
            print("Task list:")
            for index, task in enumerate(tasks, start=1):
                print(index, "-", task)
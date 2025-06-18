"""
🧠 My Program Should Be Able To:

Let the user:
    Add a new task
    View current tasks
    Remove a task by number or name
    Quit
"""

tasks = []

def show_menu():
    print("\nWhat would you like to do?")
    print("1. Add a new task")
    print("2. View current tasks")
    print("3. Remove a task by name")
    print("4. Quit\n")

    try:
        choice = int(input("Enter your choice (1 - 4): "))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            remove_task()
        elif choice == 4:
            farewell()
        else:
            print("Enter a number between 1 and 4.")
    except ValueError:
        print("Please enter a valid number.")

def add_task():
    task = input("Enter a task to add: ")
    tasks.append(task)

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

def remove_task():
    task = input("Enter a task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print(f"Removed: {task}")
    else:
        print("Task not found.")

def farewell():
    print("Goodbye!")
    exit()

# Main program loop
while True:
    show_menu()

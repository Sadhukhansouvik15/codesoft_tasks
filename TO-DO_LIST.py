def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View tasks")
    print("2. Add a new task")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
        return
    print("\nYour tasks:")
    for i, (task, completed) in enumerate(tasks, start=1):
        status = "✓" if completed else "✗"
        print(f"{i}. [{status}] {task}")

def add_task(tasks):
    task = input("Enter the new task: ").strip()
    if task:
        tasks.append((task, False))
        print(f"Task '{task}' added.")
    else:
        print("Empty task cannot be added.")

def mark_completed(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter the number of the task to mark as completed: "))
        if 1 <= index <= len(tasks):
            task, _ = tasks[index - 1]
            tasks[index - 1] = (task, True)
            print(f"Task '{task}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter the number of the task to delete: "))
        if 1 <= index <= len(tasks):
            task, _ = tasks.pop(index - 1)
            print(f"Task '{task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []

    print("Welcome to your To-Do List Manager!")

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()

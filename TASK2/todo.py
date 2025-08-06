# todo.py

def load_tasks(filename):
    """Load tasks from a file and return as a list."""
    try:
        with open(filename, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []


def save_tasks(tasks, filename):
    """Save the task list to a file."""
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')


def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def add_task(tasks):
    """Add a new task."""
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        print("Task added!")
    else:
        print("Empty task cannot be added.")


def remove_task(tasks):
    """Remove a task by its number."""
    view_tasks(tasks)
    if tasks:
        try:
            num = int(input("Enter the task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks, filename)
        elif choice == '3':
            remove_task(tasks)
            save_tasks(tasks, filename)
        elif choice == '4':
            save_tasks(tasks, filename)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

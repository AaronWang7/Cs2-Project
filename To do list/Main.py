# File to store the tasks
TODO_list_FILE = 'To do list/To_do_list.txt'

def load_tasks():
    """Load tasks from the file into a list."""
    try:
        with open(TODO_list_FILE, 'r') as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save the list of tasks to the file."""
    with open(TODO_list_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def view_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("No tasks available.")
    else:
        # Use ebumerate to make it more clear
        for i, task in enumerate(tasks, 1):
            status = "Done" if task.startswith("[Finshed!!!]") else "it will apper Finshed!!! when the task is done"
            print(f"{i}. {task} [{status}]")

def add_task(tasks):
    """Add new task to the list"""
    task = input("Enter new task: ")
    tasks.append(f"[ ] {task}")
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def delete_task(tasks):
    """Delete task from the list"""
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid/wrong task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_complete(tasks):
    """Mark task as complete."""
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            task = tasks[task_num - 1]
            if not task.startswith("[X]"):
                tasks[task_num - 1] = task.replace("[ ]", "[Finshed!!!]")
                save_tasks(tasks)
                print(f"Task '{task}' marked as complete.")
            else:
                print("Task is already marked as complete.")
        else:
            print("Invalid/Wrong task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the user choices"""
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            mark_task_complete(tasks)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid/wrong choice. Please choose a valid option.")
#make sure the program will only run when the program insn't already running
if __name__ == "__main__":
    main()

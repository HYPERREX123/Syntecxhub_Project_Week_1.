todo_list = []

def show_menu():
    print("\n----- To-Do List Menu -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task Done")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    todo_list.append({"task": task, "done": False})
    print("Task added")

def view_tasks():
    if not todo_list:
        print("No tasks yet")
        return

    print("\nYour Tasks:")
    for i, t in enumerate(todo_list, 1):
        status = "✔" if t["done"] else "✗"
        print(f"{i}. {t['task']} [{status}]")

def delete_task():
    view_tasks()
    try:
        idx = int(input("Enter task number to delete: "))
        todo_list.pop(idx - 1)
        print("Task deleted")
    except:
        print("Invalid task number")

def mark_done():
    view_tasks()
    try:
        idx = int(input("Enter task number to mark done: "))
        todo_list[idx - 1]["done"] = True
        print("Task marked as done")
    except:
        print("Invalid task number")

while True:
    show_menu()
    choice = input("Choose option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        mark_done()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")

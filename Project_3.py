import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file. If file not found, return empty list."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE,"r",encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Warning: tasks file is corrupted. Starting with an empty list")
        return []
    except Exception as e:
        print("Error loading tasks",e)
        return []

def save_tasks(tasks):
    """Save tasks list to JSON file"""
    try:
        with open(TASKS_FILE,"w",encoding="utf-8") as f:
            json.dump(tasks,f,indent=2,ensure_ascii=False)
    except Exception as e:
        print("Error saving tasks:",e)

def make_task_id(tasks):
    """Return next integer id for a new task."""
    if not tasks:
        return 1
    ids=[t.get("id",0) for t in tasks]
    return max(ids)+1

def add_task(tasks, title,tags=None, due_date=None):
    """Add a new task to the list and return it."""
    task={
        "id": make_task_id(tasks),
        "title": title,
        "done": False,
        "tags": tags or [],
        "due_date": due_date
    }
    tasks.append(task)
    return task

def find_task(tasks,task_id):
    """Find task by id. Return task or None."""
    for t in tasks:
        if t.get("id")==task_id:
            return t
    return None

def delete_task(tasks,task_id):
    """Delete a task by id. Return True if deleted."""
    task=find_task(tasks,task_id)
    if task:
        tasks.remove(task)
        return True
    return False

def mark_done(tasks, task_id):
    """Mark a task done Return True if found"""
    task=find_task(tasks,task_id)
    if task:
        task["done"]=True
        return True
    return False

def input_tags():
    s=input("Enter tags separated by commas (or leave empty): ").strip()
    if not s:
        return []
    return [tag.strip() for tag in s.split(",") if tag.strip()]

def input_due_date():
    s=input("Enter due date (YYYY-MM-DD) or leave empty: ").strip()
    if not s:
        return None
    try:
        dt=datetime.strptime(s,"%Y-%m-%d")
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Saving without due date")
        return None

def show_tasks(tasks):
    if not tasks:
        print("No tasks found")
        return
    print("\nYour tasks")
    for t in tasks:
        status = "Done" if t.get("done") else "Pending"
        tid = t.get("id")
        title = t.get("title")
        tags = ", ".join(t.get("tags", [])) if t.get("tags") else "No tags"
        due = t.get("due_date") or "No due date"
        print(f"[{tid}] {title}  ({status})")
        print(f"     Tags: {tags}  Due: {due}")
    print()

def menu():
    tasks=load_tasks()
    while True:
        print("\nTo-Do List Manager")
        print("------------------")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task done")
        print("5. Exit")
        choice=input("Choose an option (1-5): ").strip()

        if choice=="1":
            show_tasks(tasks)

        elif choice == "2":
            title=input("Task title: ").strip()
            if not title:
                print("Title cannot be empty")
                continue
            tags=input_tags()
            due=input_due_date()
            new_task=add_task(tasks,title,tags,due)
            save_tasks(tasks)
            print(f"Added task [{new_task['id']}]")

        elif choice=="3":
            try:
                tid=int(input("Enter task id to delete: "))
            except ValueError:
                print("Please enter a valid integer id")
                continue
            if delete_task(tasks, tid):
                save_tasks(tasks)
                print("Task deleted")
            else:
                print("Task id not found")

        elif choice=="4":
            try:
                tid=int(input("Enter task id to mark done: "))
            except ValueError:
                print("Please enter a valid integer id")
                continue
            if mark_done(tasks,tid):
                save_tasks(tasks)
                print("Task marked as done")
            else:
                print("Task id not found")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 5")

if __name__=="__main__":
    menu()
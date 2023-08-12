# begginer todo-list project


# todo_list.py

tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})

def view_tasks():
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{index}. [{status}] {task['task']}")

def complete_task(index):
    if 0 < index <= len(tasks):
        tasks[index - 1]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Completed\n4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            index = int(input("Enter task index to mark as completed: "))
            complete_task(index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

task_list = ["Buy groceries", "Complete assignment", "Read book"]
user_list = ["Admin", "User1", "User2"]
completed_list = ["Read book"]
while True:
    print("\n===== TASK MANAGEMENT SYSTEM =====")
    print("1. ADMIN")
    print("2. USER")
    print("3. EXIT")
    choice = input("Select role: ")
    if choice == "1":
        while True:
            print("\n----- ADMIN SECTION -----")
            print("1. Add Task")
            print("2. Update Task")
            print("3. Delete Task")
            print("4. View All Tasks")
            print("5. View Users")
            print("6. Exit")
            ch = input("Enter choice: ")
            if ch == "1":
                task = input("Enter task: ")
                task_list.append(task)
                print("Task added successfully")
            elif ch == "2":
                print("\nTasks:")
                for task in task_list:
                    print(task)
                old = input("Enter task to update: ")
                if old in task_list:
                    new = input("Enter new task: ")
                    index = task_list.index(old)
                    task_list[index] = new
                    print("Task updated successfully")
                else:
                    print("Task not found")
            elif ch == "3":
                print("\nTasks:")
                for task in task_list:
                    print(task)
                task = input("Enter task to delete: ")
                if task in task_list:
                    task_list.remove(task)
                    if task in completed_list:
                        completed_list.remove(task)
                    print("Task deleted successfully")
                else:
                    print("Task not found")
            elif ch == "4":
                print("\n----- ALL TASKS -----")
                for task in task_list:
                    if task in completed_list:
                        print(task, "- Completed")
                    else:
                        print(task, "- Pending")
            elif ch == "5":
                print("\n----- USERS -----")
                for user in user_list:
                    print(user)
            elif ch == "6":
                break
            else:
                print("Invalid choice")
    elif choice == "2":
        while True:
            print("\n----- USER SECTION -----")
            print("1. View My Tasks")
            print("2. Add Task")
            print("3. Update My Task")
            print("4. Delete My Task")
            print("5. Mark Task Complete")
            print("6. Exit")
            ch = input("Enter choice: ")
            if ch == "1":
                print("\n----- MY TASKS -----")
                for task in task_list:
                    if task in completed_list:
                        print(task, "- Completed")
                    else:
                        print(task, "- Pending")
            elif ch == "2":
                task = input("Enter task: ")
                task_list.append(task)
                print("Task added successfully")
            elif ch == "3":
                old = input("Enter task to update: ")
                if old in task_list:
                    new = input("Enter new task: ")
                    index = task_list.index(old)
                    task_list[index] = new
                    print("Task updated successfully")
                else:
                    print("Task not found")
            elif ch == "4":
                task = input("Enter task to delete: ")
                if task in task_list:
                    task_list.remove(task)
                    if task in completed_list:
                        completed_list.remove(task)
                    print("Task deleted successfully")
                else:
                    print("Task not found")
            elif ch == "5":
                task = input("Enter completed task: ")
                if task in task_list:
                    if task not in completed_list:
                        completed_list.append(task)
                        print("Task marked as completed")
                    else:
                        print("Task already completed")
                else:
                    print("Task not found")
            elif ch == "6":
                break
            else:
                print("Invalid choice")
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice")


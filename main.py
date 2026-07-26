from manager import TodoManager

manager = TodoManager()

while True:
    print("\n===== TODO MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter task title: ")
        important = input("Is it important? (y/n): ").lower() == "y"
        manager.add_task(title, important)

    elif choice == "2":
        manager.view_tasks()

    elif choice == "3":
        manager.view_tasks()
        index = int(input("Enter task number to complete: ")) - 1
        manager.complete_task(index)

    elif choice == "4":
        manager.view_tasks()
        index = int(input("Enter task number to delete: ")) - 1
        manager.delete_task(index)

    elif choice == "5":
        print("Thank you for using Todo Manager.")
        break

    else:
        print("Invalid choice. Please try again.")
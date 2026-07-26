from task import Task, ImportantTask
from storage import Storage
class TodoManager:
    def __init__(self):
        self.tasks = Storage.load_tasks()

    def add_task(self, title, important=False):
        if important:
            task = ImportantTask(title)
        else:
            task = Task(title)

        task_data = {
            "title": task.title,
            "completed": task.completed,
            "priority": getattr(task, "priority", "Normal")
        }

        self.tasks.append(task_data)
        Storage.save_tasks(self.tasks)

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks found.\n")
            return

        print("\n------ TASK LIST ------")
        for i, task in enumerate(self.tasks, start=1):
            status = "✔" if task["completed"] else "✘"
            print(f"{i}. {task['title']} [{status}] ({task['priority']})")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            Storage.save_tasks(self.tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            Storage.save_tasks(self.tasks)
            print("Task deleted.")
        else:
            print("Invalid task number.")
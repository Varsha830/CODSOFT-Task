import os

class TodoListCLI:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Save Tasks to File")
        print("6. Load Tasks from File")
        print("7. Exit")

    def add_task(self):
        task = input("Enter task: ")
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("\n===== Tasks =====")
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{idx}. [{status}] {task['task']}")

    def mark_completed(self):
        self.view_tasks()
        try:
            task_idx = int(input("Enter task number to mark as completed: ")) - 1
            self.tasks[task_idx]["completed"] = True
            print(f"Task '{self.tasks[task_idx]['task']}' marked as completed.")
        except IndexError:
            print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def remove_task(self):
        self.view_tasks()
        try:
            task_idx = int(input("Enter task number to remove: ")) - 1
            task_name = self.tasks[task_idx]["task"]
            del self.tasks[task_idx]
            print(f"Task '{task_name}' removed successfully.")
        except IndexError:
            print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def save_tasks_to_file(self):
        file_name = input("Enter file name to save tasks (e.g., tasks.txt): ")
        try:
            with open(file_name, 'w') as f:
                for task in self.tasks:
                    f.write(f"{task['task']},{task['completed']}\n")
            print(f"Tasks saved to '{file_name}' successfully.")
        except IOError:
            print(f"Error saving tasks to '{file_name}'.")

    def load_tasks_from_file(self):
        file_name = input("Enter file name to load tasks from: ")
        if os.path.exists(file_name):
            try:
                self.tasks = []
                with open(file_name, 'r') as f:
                    for line in f:
                        task_name, completed = line.strip().split(',')
                        self.tasks.append({"task": task_name, "completed": bool(completed)})
                print(f"Tasks loaded from '{file_name}' successfully.")
            except IOError:
                print(f"Error loading tasks from '{file_name}'.")
        else:
            print(f"File '{file_name}' not found.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.mark_completed()
            elif choice == '4':
                self.remove_task()
            elif choice == '5':
                self.save_tasks_to_file()
            elif choice == '6':
                self.load_tasks_from_file()
            elif choice == '7':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a valid option (1-7).")

if __name__ == "__main__":
    todo_app = TodoListCLI()
    todo_app.run()

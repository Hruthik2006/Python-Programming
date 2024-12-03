# To-Do list  

from datetime import datetime

class Task:
    def _init_(self, description, due_date:None, priority:None):
        self.description description
        self.due date due date
        self.priority priority
        self.completed: False
        
    def str (self):
        status "Completed" if self.completed else "Incomplete"
        return f"Task: (self.description), Due: (self.due_date), Priority: (self.priority), Status: (status)"

class ToDoList:
    def _init_(self):
        self.tasks = []
        
    def add_task(self, description, due_date=None, priority=None):
        task Task(description, due_date, priority)
        self.tasks.append(task)
        print(f"Task added: {description}")
        
    def delete_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            removed_task = self.tasks.pop(task_id) print(f"Task deleted: {removed_task.description}")
        else:
            print("Invalid task ID")
            
    def view_tasks (self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for idx, task in enumerate(self.tasks):
            print(f"(idx). {task}")
            
    def mark_task_completed(self, task_id):
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id].completed = True
            print(f"Task marked as completed: {self.tasks[task_id].description}")
        else:
            print("Invalid task ID")

todo_list ToDoList()

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Mark Task as Completed")
    print("5. Exit")
    choice input("Choose an option (1-5): ")
    
    if choice == "1":
        description = input("Enter the task description: ")
        due_date_input = input("Enter the due date (YYYY-MM-DD) or leave blank: ")
        due_date due_date_input if due_date_input else None
        priority= input("Enter the priority (High, Medium, Low) or leave blank: ")
        todo_list.add_task(description, due_date, priority)
    elif choice == "2":
        task_id=int(input("Enter the task ID to delete: "))
        todo_list.delete_task(task_id)
    elif choice == "3":
        todo_list.view_tasks()
    elif choice == "4":
        task_id= int(input("Enter the task ID to mark as completed: "))
        todo_list.mark_task_completed(task_id)
    elif choice == "5":
        print("Exiting the to-do list application. Goodbye!") break
    else:
        print("Invalid choice. Please try again.")

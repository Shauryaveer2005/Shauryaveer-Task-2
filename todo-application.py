import tkinter as tk
from tkinter import messagebox
import json
import os
class ToDo:
    def __init__(self, filename="todo.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        else:
            return []

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()

    def complete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["completed"] = True
            self.save_tasks()

    def delete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks.pop(task_number)
            self.save_tasks()

        
class ToDoApp(tk.Tk):
    def __init__(self, todo):
        super().__init__()
        self.todo = todo
        self.title("ToDo Application")
        self.geometry("400x400")

        # Task Entry
        self.task_entry = tk.Entry(self, width=40)
        self.task_entry.pack(pady=10)

        # Add Task Button
        self.add_task_button = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Task Listbox
        self.task_listbox = tk.Listbox(self, selectmode=tk.SINGLE, width=40, height=15)
        self.task_listbox.pack(pady=10)
        self.populate_listbox()

        # Complete Task Button
        self.complete_task_button = tk.Button(self, text="Complete Task", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        # Delete Task Button
        self.delete_task_button = tk.Button(self, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

    def populate_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.todo.tasks):
            status = "✓" if task["completed"] else "✗"
            self.task_listbox.insert(tk.END, f"{idx+1}. [{status}] {task['task']}")

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo.add_task(task)
            self.task_entry.delete(0, tk.END)
            self.populate_listbox()

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.todo.complete_task(task_index)
            self.populate_listbox()
        else:
            messagebox.showwarning("Select Task", "Please select a task to complete.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.todo.delete_task(task_index)
            self.populate_listbox()
        else:
            messagebox.showwarning("Select Task", "Please select a task to delete.")
if __name__ == "__main__":
    todo = ToDo()
    app = ToDoApp(todo)
    app.mainloop()

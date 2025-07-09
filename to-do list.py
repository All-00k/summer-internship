import tkinter as tk
from tkinter import messagebox
from tkinter import *

from tkcalendar import DateEntry
import json
import os


TASK_FILE = "tasks.json"

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("800x800")
        self.root.config(bg="grey")

        Label(root, text="Summer Internship Project", font=("Arial", 12, "bold")).pack(pady=5)
        Label(root, text="Made by: Alok Singh Yadav", font=("Arial", 10)).pack(pady=2)
        Label(root, text="Branch: CSE-DS | Year: 1st", font=("Arial", 10)).pack(pady=2)

        self.title_label = tk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold"), bg="lightblue")
        self.title_label.pack(padx=10,pady=10)


        self.task_entry = tk.Entry(root, font=("Helvetica", 14), width=30,bg='white')
        self.task_entry.pack(padx=10,pady=10)

        tk.Label(root, text="Due Date:", font=("Helvetica", 12), bg="white").pack()
        self.date_entry = DateEntry(root, width=12, background='darkblue',foreground='white', borderwidth=2, font=("Helvetica", 12), date_pattern = 'yyyy-mm-dd')
        self.date_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add The Task", width=25, command=self.add_task)
        self.add_button.pack()


        self.task_listbox = tk.Listbox(root, font=("Helvetica", 15), width=50, height=18, selectbackground="blue")
        self.task_listbox.pack(pady=10)


        self.delete_button = tk.Button(root, text="Delete Selected", width=15, command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Mark as Complete", width=15, command=self.mark_complete)
        self.complete_button.pack(pady=5)

        self.delete_all_button = tk.Button(root, text="Delete All Task", width=15, command=self.delete_all_task,)
        self.delete_all_button.pack(padx=5,pady=5)


        self.tasks = []
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get().strip().title()
        due_date = self.date_entry.get_date().strftime('%Y-%m-%d')
        if task == "":
            messagebox.showwarning("Input Error", "Task cannot be empty!")
            return
        self.tasks.append({"text": task,"date": due_date, "completed": False})
        self.task_entry.delete(0, tk.END)
        self.refresh_listbox()
        self.save_tasks()


    def delete_task(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")
            return
        index = selected[0]
        self.tasks.pop(index)
        self.refresh_listbox()
        self.save_tasks()

    def delete_all_task(self):

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete all tasks?")
        if confirm:
            self.tasks = []
            self.task_listbox.delete(0, tk.END)

            self.save_tasks()

    def mark_complete(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a task to mark complete.")
            return
        index = selected[0]
        self.tasks[index]["completed"] = not self.tasks[index]["completed"]
        self.refresh_listbox()
        self.save_tasks()

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✔️ " if task["completed"] else ""
            display = f"{status}{task['text']}  (Due: {task['date']})"
            self.task_listbox.insert(tk.END, display)

    def save_tasks(self):
        with open(TASK_FILE, "w") as file:
            json.dump(self.tasks, file)

    def load_tasks(self):
        if os.path.exists(TASK_FILE):
            with open(TASK_FILE, "r") as file:
                self.tasks = json.load(file)
            self.refresh_listbox()

# Main App
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoList(root)
    root.mainloop()

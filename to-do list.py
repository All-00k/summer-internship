import tkinter as tk
from tkinter import messagebox
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

        # ----- Scrollable canvas setup -----
        canvas = tk.Canvas(root, bg="grey", highlightthickness=0)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)

        # Frame inside canvas
        main_frame = tk.Frame(canvas, bg="grey")
        canvas.create_window((0, 0), window=main_frame, anchor="nw")

        # Update scrollregion on frame resize
        main_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Enable mouse wheel scrolling
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

        # ----- All UI elements inside main_frame -----
        tk.Label(main_frame, text="Summer Internship Project", font=("Arial", 12, "bold"), bg="grey").pack(pady=5)
        tk.Label(main_frame, text="Made by: Alok Singh Yadav", font=("Arial", 10), bg="grey").pack(pady=2)
        tk.Label(main_frame, text="Branch: CSE-DS | Year: 1st", font=("Arial", 10), bg="grey").pack(pady=2)

        self.title_label = tk.Label(main_frame, text="To-Do List", font=("Helvetica", 18, "bold"), bg="lightblue")
        self.title_label.pack(padx=10, pady=10)

        self.task_entry = tk.Entry(main_frame, font=("Helvetica", 14), width=30, bg='white')
        self.task_entry.pack(padx=10, pady=10)

        tk.Label(main_frame, text="Due Date:", font=("Helvetica", 12), bg="white").pack()
        self.date_entry = DateEntry(main_frame, width=12, background='darkblue', foreground='white', borderwidth=2, font=("Helvetica", 12), date_pattern='yyyy-mm-dd')
        self.date_entry.pack(pady=5)

        self.add_button = tk.Button(main_frame, text="Add The Task", width=25, command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(main_frame, font=("Helvetica", 15), width=50, height=18, selectbackground="blue")
        self.task_listbox.pack(pady=10)

        self.delete_button = tk.Button(main_frame, text="Delete Selected", width=15, command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(main_frame, text="Mark as Complete", width=15, command=self.mark_complete)
        self.complete_button.pack(pady=5)

        self.delete_all_button = tk.Button(main_frame, text="Delete All Task", width=15, command=self.delete_all_task)
        self.delete_all_button.pack(padx=5, pady=5)

        # Load tasks
        self.tasks = []
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get().strip().title()
        due_date = self.date_entry.get_date().strftime('%Y-%m-%d')
        if task == "":
            messagebox.showwarning("Input Error", "Task cannot be empty!")
            return
        self.tasks.append({"text": task, "date": due_date, "completed": False})
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

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoList(root)
    root.mainloop()

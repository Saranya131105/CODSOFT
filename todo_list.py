import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3 as sql

connection = sql.connect('tasks.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT, completed BOOLEAN)')
connection.commit()

class ToDoApp:
    def __init__(self, root):  
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x600")
        self.root.configure(bg="#E0F7FA")
        self.tasks = []
        self.load_tasks()
        
        header = tk.Label(self.root, text="My Tasks", font=("Comic Sans MS", 24, "bold"), bg="#E0F7FA", fg="#00796B")
        header.pack(pady=20)
        
        frame = tk.Frame(self.root, bg="#E0F7FA")
        frame.pack(expand=True, fill="both")
        
        self.canvas = tk.Canvas(frame, bg="#E0F7FA", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(frame, orient="vertical", command=self.canvas.yview)
        
        self.task_frame = tk.Frame(self.canvas, bg="#E0F7FA")
        self.task_frame.bind(
            "<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((20, 0), window=self.task_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        self.task_entry = tk.Entry(self.root, font=("Comic Sans MS", 14))
        self.task_entry.pack(pady=10)
        
        add_button = tk.Button(self.root, text="+", command=self.add_task, font=("Comic Sans MS", 14), bg="#00796B", fg="white", width=3)
        add_button.pack()
        
        self.display_tasks()
    
    def load_tasks(self):
        cursor.execute('SELECT * FROM tasks')
        rows = cursor.fetchall()
        self.tasks = [{"id": row[0], "title": row[1], "completed": row[2]} for row in rows]
    
    def display_tasks(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()
        for index, task in enumerate(self.tasks):
            self.create_task_widget(task, index)
    
    def create_task_widget(self, task, index):
        var = tk.BooleanVar(value=task["completed"])
        check_button = tk.Checkbutton(
            self.task_frame,
            variable=var,
            font=("Comic Sans MS", 14),
            bg="#E0F7FA",
            fg="#00796B" if task["completed"] else "black",
            command=lambda: self.toggle_task(task, var)
        )
        check_button.grid(row=index, column=0, sticky="w", padx=5, pady=5)
        
        task_label = tk.Label(
            self.task_frame,
            text=task["title"],
            font=("Comic Sans MS", 14),
            bg="#E0F7FA",
            fg="#00796B" if task["completed"] else "black",
            cursor="hand2"
        )
        task_label.grid(row=index, column=1, sticky="w", padx=10, pady=5)
        task_label.bind("<Button-1>", lambda e: self.edit_task(task))
    
    def add_task(self):
        task_title = self.task_entry.get().strip()
        if task_title == "":
            messagebox.showwarning("Warning", "Please enter a task title.")
            return
        cursor.execute('INSERT INTO tasks (title, completed) VALUES (?, ?)', (task_title, False))
        connection.commit()
        self.tasks.append({"id": cursor.lastrowid, "title": task_title, "completed": False})
        self.task_entry.delete(0, tk.END)
        self.display_tasks()
    
    def toggle_task(self, task, var):
        task["completed"] = var.get()
        cursor.execute('UPDATE tasks SET completed = ? WHERE id = ?', (task["completed"], task["id"]))
        connection.commit()
        self.display_tasks()
    
    def edit_task(self, task):
        new_title = simpledialog.askstring("Edit Task", "Modify task title:", initialvalue=task["title"])
        if new_title and new_title.strip() != "":
            task["title"] = new_title.strip()
            cursor.execute('UPDATE tasks SET title = ? WHERE id = ?', (task["title"], task["id"]))
            connection.commit()
            self.display_tasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
    connection.close()

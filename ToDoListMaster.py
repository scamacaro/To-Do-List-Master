"""
Sanyerlis Camacaro - CSC235 - Sancamac@uat.edu Assignment:
How to create a GUI in Python.

"To Do List Master"
A Simple Python Program that has a GUI that acts as a To Do List.
The user can add items to the list, and mark them as done when they're finished.
The user can also delete tasks and ask for help on how to use the application.

This code demonstrates how to:
Create a GUI program in Python
Make sense and have a theme not just be a demo of a GUI.
Make a great User experience.
Over comment your code showing your intent and your understanding of what your code does.


"""

# This line imports the tkinter module which provides a powerful object-oriented interface to the Tk GUI toolkit.
import tkinter as tk
# This imports the messagebox module which provides a set of dialog boxes from tkinter.
from tkinter import messagebox


def show_help():
    # Define the text for the help message
    help_text = """
    1. Add Task: Enter a task in the text field and click 'Add Task'.
    2. Mark as Done: Select a task and click 'Mark as Done' to indicate that you have completed the task. 
    The task will be prefixed with '[DONE]'.
    3. Delete: Select a task and click 'Delete' to remove the task from the list.
    """
    # Show the help message
    messagebox.showinfo("Help", help_text)


# This line starts the definition of the TodoApp class.
class TodoApp:
    # This is the constructor method for the TodoApp class.
    def __init__(self, master):
        self.master = master
        # : This line sets the title of the window to "To-Do List Master".
        self.master.title("To-Do List Master")
        #  This sets the geometry of the window to 300 pixels wide and 400 pixels tall.
        self.master.geometry("300x400")

        # This initializes the tasks attribute as an empty list. It will hold the tasks that the user enters.
        self.tasks = []

        # This line creates a new frame widget in the master window.
        self.entry_frame = tk.Frame(self.master)
        self.entry_frame.pack(fill=tk.X, padx=5, pady=5)

        # This packs the Entry widget into the frame.
        self.task_entry = tk.Entry(self.entry_frame, width=25)
        self.task_entry.pack(side=tk.LEFT, padx=5, pady=5)

        # This creates a new Button widget with the text "Add Task"
        self.add_task_button = tk.Button(self.entry_frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(side=tk.RIGHT, padx=5)

        #  This creates another Frame widget in the master window.
        self.list_frame = tk.Frame(self.master)
        self.list_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # This creates a Scrollbar widget in the list_frame.
        self.scrollbar = tk.Scrollbar(self.list_frame)

        self.task_listbox = tk.Listbox(self.list_frame, yscrollcommand=self.scrollbar.set, selectmode=tk.MULTIPLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar.config(command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(fill=tk.X, padx=5, pady=5)

        # This creates a Button for marking tasks as done.
        self.done_button = tk.Button(self.button_frame, text="Mark as Done", command=self.mark_done)
        self.done_button.pack(side=tk.LEFT, padx=5)

        # This creates a Button for deleting tasks.
        self.delete_button = tk.Button(self.button_frame, text="Delete", command=self.delete_task)
        self.delete_button.pack(side=tk.RIGHT, padx=5)

        # This creates a 'Help' button.
        self.help_button = tk.Button(self.button_frame, text="Help", command=show_help)
        self.help_button.pack(side=tk.LEFT, padx=5)

        # This starts the definition of the add_task method.

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.tasks.append(task)
        else:
            messagebox.showerror("Error", "Please enter a task.")
        self.task_entry.delete(0, tk.END)

        # This starts the definition of the mark_done method.

    def mark_done(self):
        selected_tasks = self.task_listbox.curselection()
        for selected_task in selected_tasks:
            self.task_listbox.delete(selected_task)
            self.task_listbox.insert(selected_task, "[DONE] " + self.tasks[selected_task])
            self.tasks[selected_task] = "[DONE] " + self.tasks[selected_task]

            # This starts the definition of the delete_task method.

    def delete_task(self):
        selected_tasks = self.task_listbox.curselection()
        for selected_task in selected_tasks[::-1]:
            self.task_listbox.delete(selected_task)
            del self.tasks[selected_task]


root = tk.Tk()  # This creates the main application window.
todo_app = TodoApp(root)  # This creates a new TodoApp object.
root.mainloop()  # This starts the main event loop.

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("GUI")

# Functions
def new_file():
    messagebox.showinfo("New", "New file created!")

def open_file():
    messagebox.showinfo("Open", "Open file dialog here")

def show_about():
    messagebox.showinfo("About", "My First GUI App\nVersion 1.0")

# Menu bar
menu = tk.Menu(root)
root.config(menu=menu)

# File menu
filemenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open...", command=open_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

# Help menu
helpmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=show_about)

root.mainloop()
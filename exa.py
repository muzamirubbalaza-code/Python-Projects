import tkinter as tk
from tkinter import messagebox


def openMessageBox():
    messagebox.showinfo(title="Info Message", message="This is an Info Message")
    messagebox.showerror(title="Error",message="You Made an Error!")
    messagebox.showwarning(title="Warning!",message="This is a Warning!")
    messagebox.askquestion(title="Question",message="Do You Wish to Proceed?")
    messagebox.askyesno(title="Question",message="Do You Wish to Continue?")
    messagebox.askretrycancel(title="Question",message="Do you want to Retry?")
    messagebox.askokcancel(title="Question",message="Do you want to Retry?")
    messagebox.askyesnocancel(title="Question",message="Do you want to Retry?")


window = tk.Tk()
window.title("Message Box Practice")
button = tk.Button(window,
                   text="Press Me",
                   command=openMessageBox)
button.pack()
window.mainloop()
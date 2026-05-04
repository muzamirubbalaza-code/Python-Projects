import tkinter as tk
from tkinter import messagebox


class TodoApp:  # This class will contain all the content which makes the app to be more organised
    def __init__(self,root): # Instructor of the entire class and root is the main application window
        self.root = root # Configuring the main window; storing the main window inside the class so that i can use it anywhere in the class
        self.root.title("To-Do List")
        self.root.geometry("500x450")
        self.root.resizable(False,False) # This disables resizing from both horizontal and vertical so that the user can drag the edges of the window
        self.root.configure(bg="#F0F4F7")


        self.tasks = [] # This will contain all our tasks as dictionaries with texts as tasks
        self.setup_ui() # This will build the entire user interface


    def setup_ui(self):
        title_label = tk.Label(
            self.root,# So that label belongs to the main window (root)
            text="To-Do List",
            font=("Helvetica",22,"bold"),
            bg="#F0F4F7",
            fg="#333"
        ).pack(pady=10) # This places it at the top with some spacing

        input_frame = tk.Frame(self.root,bg="#F0F4F7")
        input_frame.pack(pady=10)

        self.task_entry = tk.Entry( #This sets up the main textarea for the to-do tasks entered by the user into the App
            input_frame,
            font=("Helvetica",12),
            width=30
        )
        self.task_entry.pack(side="left",padx=(0,10)) #Placed on the lefthand side with some padding on the right

        add_button = tk.Button(
            input_frame, #This makes the Button and the entry to be renderd side by side in a single row
            text="Add Task", 
            font=("Helvetica",11,"bold"),
            bg="#27ae60",
            fg="white",
            pady=10,
            command= self.add_task # This instructs the computer to run app when the user clicks the button
        )
        add_button.pack(side="left")

        #Setting up the space where all the tasks will appear on the App
        list_frame = tk.Frame(self.root,bg="#F0F4F7")
        list_frame.pack(pady=10,expand=True,fill="both") #This allows the frame to stretch and take up the available space 

        #Inserting a listbox that renders (displays) all of our tasks
        self.task_listbox = tk.Listbox(
            list_frame,
            font=("Helvetica",12),
            width=45,
            height=10,
            activestyle=None #Tis line removes the default highlight styling and makes the entire box cleaner
        )
        self.task_listbox.pack(side="left",fill="both",expand=True)

        #Creating the scrollbar for the tasks and putting it on the righthand side so that it stretches vertically along the tasks in the frame.
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right",fill="y") 

        #Connecting the scrollbar and the listbox together
        self.task_listbox.config(yscrollcommand=scrollbar.set) #This allows the scrollbar to update it's position based on the scrolling of the list.
        scrollbar.config(command=self.task_listbox.yview) #This line instructs the scrollbar to scroll when action is performed on it by the user

        #Adding a small textarea under the list and use it as the text messages
        self.info_label = tk.Label(
            self.root, #This is because this label belongs to the main window not the list frame
            text="",#Empty becoz we will update it dynamically as the user interact with the App
            font=("Helvetica",11),
            bg="#F0F4F7",
            fg="#007acc"
        )
        self.info_label.pack(pady=5)


        #Bulding the bottom section of the app so that the user manages the tasks 
        button_frame = tk.Frame(self.root,bg="#F0F4F7")
        button_frame.pack(pady=10)

        markdone_button = tk.Button(
            button_frame,
            text="Mark As Done",
            font=("Helvetica",11,"bold"),
            bg="#2980b9",
            fg="white",
            padx=10,
            command= self.mark_done #This will run the markdone method or function when the clicked.
        )
        markdone_button.pack(side="left",padx=5)

        delete_button = tk.Button(
            button_frame,
            text="Delete Task",
            font=("Helvetica",11,"bold"),
            bg="#c0392b",
            fg="white",
            padx=10,
            command=self.delete_task #Calls the delete method or function when clicked
        )
        delete_button.pack(side="left",padx=5)

        clear_button = tk.Button(
            button_frame,
            text="Clear All",
            font=("Helvetica",11,"bold"),
            bg="#7f8c8d",
            fg="white",
            padx=10,
            command=self.clear_all #Calls the clear method when clicked by the user
        )
        clear_button.pack(side="left",padx=5)

    #Adding the logic behind the Buttons 
    def refresh_listbox(self):
        self.task_listbox.delete(0,tk.END) #This removes every single row that is currently displayed
        for index,task in enumerate(self.tasks,start=1):
            status = "\u2705" if task["done"] else "\u274c"
            display_text = f"{index}.{task['task']} [{status}]"
            self.task_listbox.insert(tk.END,display_text) #This adds a newline at the bottom of the listbox
    
    #Adding the add task method that runs when you click on the Add Task Button
    def add_task(self):
        task_text = self.task_entry.get().strip() #Getting what the user types and removes any spaces 
        #Checking whether the task_text is empty
        if not task_text:
            self.info_label.config(text="Please Enter A Task First.")
            return
        
        self.tasks.append({"task":task_text ,"done":False})
        self.task_entry.delete(0,tk.END)
        self.info_label.config(text=f"Task'{task_text} added!") #Informs the user that task is being added
        self.refresh_listbox()

    def get_selected_index(self):
        selection = self.task_listbox.curselection() #Returns a couple of selected indexes
        #Checking if the selection is empty and show popup messages
        if not selection:
            messagebox.showinfo("No Selection","Please Select a task first.")
            return None
        return selection[0] #This Index corresponds to the first task selected by the user

    def mark_done(self):
            index = self.get_selected_index()
            if index is None:
                return # (For this case if no task selected: return nothing)
            
            self.tasks[index]["done"] = True
            self.info_label.config(text="Task marked as Done!") #This gives immediate feedback to the user that task was successful
            self.refresh_listbox()
    
    def delete_task(self):
        index = self.get_selected_index()
        if index is None:
            return

        removed = self.tasks.pop(index)
        self.info_label.config(text=f"Deleted task: {removed['task']}")
        self.refresh_listbox()

    def clear_all(self):
        #Checking if the tasks list is empty;whether no task selected and then update it to info_label
        if not self.tasks:
            self.info_label.config(text="No Tasks to Clear")
            return #(We return becoz there is nothing much to do)
        
        if messagebox.askyesno("Clear All", "Are You Sure you want to delete all tasks?"):
            #If the user clicks yes then the following methods take control.
            self.tasks.clear()
            self.refresh_listbox()
            self.info_label.config(text="All Tasks Cleared!")

#Creating the main window and lauch the application
#Line 178 means only run the code in this block if this file is done directly as a script and not being imported from somewhere else
if __name__ == "__main__":
    root = tk.Tk() #This creates a new window of tkinter and store it in the root variable
    app = TodoApp(root)#This calls the init method of the app class 
    root.mainloop() #This line starts up the application


# Graphical User Interfaces : A place where the users can interact with the program created 
# Tkinter library 
# Pattern to follow :  4-step pattern 
# pattern 1:  importing the Tkinker library and give it a name E.g "Tk"
#Pattern 2: Creating and Labelling the frame (Name , width and Height)
#Pattern 4: Creating of Widgets
#Pattern 3: Starting the applications  

# Programs
import tkinter as tk

root = tk.Tk() # Frame Creation
root.title("My First GUI") #Naming our application
root.geometry("400x400") #Setting the width and the height

widget = tk.Label(
    root,
    text="My First GUI",
     fg="white",
     bg="black",
     font=("Times New Roman",30,"bold"),  
     padx=10 , pady=10       
                )
button = tk.Button(
    root,
    text="Click Me",
    bg="blue",
    fg="black",
    activebackground="black",
    activeforeground="white",
    font=("Plus Sans Jakarta",28),
    bd=5, # Setting the width
    relief="raised",
    )

def clicked():
    print("Button Clicked!")

button = tk.Button(root, text="Click Me", command=clicked)

widget.pack()
button.pack()

root.mainloop() #Starting the application
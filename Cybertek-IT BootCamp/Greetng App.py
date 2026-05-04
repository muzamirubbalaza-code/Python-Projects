import tkinter as tk

# Step1: define the function Before the widgets
def greet():
    name=name_entry.get()# we are reading what the user types
    city=city_entry.get()

    if name=="":
        result_label.config(text="Please enter your name and city", fg="#CC2222")
        return
    name = name.strip().title()
    city = city.strip().title()
    if city:
        message = f"Hello, {name}! Greetings from {city}"
    else:
        message = f"Hello, {name}! Welcome to Cyberteks-IT"

    result_label.config(text=message, fg="#0D2252")



#Step2: Creating the main window

myRoot = tk.Tk()
myRoot.title("Cyberteks-IT - Creeter App")
myRoot.geometry("420x280")
myRoot.configure(bg="#F4F7FC")
myRoot.resizable(False, False)

#Step3 : Add a title label
tk.Label(myRoot,
         text="Hello, Cyberteks-IT - Creeter App",
         bg="#0D2252",
         fg="white",
         font=("Arial", 13, "bold"),
         pady=8
         ).pack(fill='x')

#Step4: Name field
tk.Label(myRoot,
         text="Enter you name:",
         bg="#F4F7FC",
         anchor="w",
         font=("Arial",11)
         ).pack(padx=20, pady=(14,2), fill='x')

name_entry = tk.Entry(myRoot, width=40, font=("Arial", 11))
name_entry.pack(padx=20, pady=(0,10))
name_entry.focus() # cursor tarts here automatically


#Step5: City field
tk.Label(myRoot,
         text="Enter you City",
         bg="#F4F7FC",
         anchor="w",
         font=("Arial",11)
         ).pack(padx=20, pady=(0,2), fill='x')
city_entry = tk.Entry(myRoot, width=40, font=("Arial", 11))
city_entry.pack(padx=20, pady=(0,12))

# Step6:  Button which links to the function
tk.Button(myRoot,
          text="Say Hello!",
          command=greet,
          bg="#0D2252", fg="blue",
          padx=20, pady=6
          ).pack()

#Step 7: result label
result_label = tk.Label(myRoot, text='',
                        bg='#F4F7FC',
                        font=('Arial', 12, 'bold'),
                        wraplength=380)
result_label.pack(pady=14)
myRoot.bind('<Return>', lambda e: greet())

myRoot.mainloop()
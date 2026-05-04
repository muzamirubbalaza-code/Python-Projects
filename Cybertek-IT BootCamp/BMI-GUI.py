import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
# Personal Details
        name = name_entry.get().strip().title()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if height <= 0:
            raise ValueError('Height must be greater than 0')
        #Bmi Calculation
        bmi=round( weight / (height**2) , 2)

        # Categories

        if bmi<18.5:
            category,color="underweight","#BB91B2"

        elif 25.0 > bmi >= 18.5:
            category, color="normal","#15803D"
        
        elif 29.9 > bmi >= 25.0:
            category , color="overweight","#B45309"
        
        else:
            category , color="Obese","#CC2222"
        

        if name:
            result_label.config(
                text=f'{bmi} | {category}',
                fg=color
            )
    except ValueError as e:
        result_label.config(
            text=f'Error:{e}',
            fg="#CC2222"
        )            

def clear_fields():
    name_entry.delete(0,tk.END) 
    weight_entry.delete(0,tk.END)
    height_entry.delete(0,tk.END)
    result_label.config(text="",fg="black")  
    name_entry.focus()


#Creating the Graphical User Interface
root = tk.Tk()
root.title('BMI CALCULATOR')
root.geometry("400x288") 
root.configure(bg="#F4F7FC")
root.resizable(False,False)

tk.Label(root,text="Cyberteks-IT BMI Calculator",
         bg="#0D2252",fg="white", font=("Arial",12,"bold"),
         pady=8
         ).grid(row=0,columnspan=2,column=0)

#name
tk.Label(root, text="Name (optional):",
         bg="#F4F7FC", font=("Arial", 10)
         ).grid(row=1, column=0, pady=(16, 6), padx=(20, 8))
name_entry= tk.Entry(root, width=22, font=("Arial", 10))
name_entry.grid(row=1, column=1, padx=(0,20), pady=6)
#weight
tk.Label(root, text="Weight(kg):",
         bg="#F4F7FC", font=("Arial", 10)
         ).grid(row=2, column=0, pady=(16, 6), padx=(20, 8))
weight_entry= tk.Entry(root, width=22, font=("Arial", 10))
weight_entry.grid(row=2, column=1, padx=(0,20), pady=6)
#height
tk.Label(root, text="Height(m):",
         bg="#F4F7FC", font=("Arial", 10)
         ).grid(row=3, column=0, pady=(16, 6), padx=(20, 8))
height_entry= tk.Entry(root, width=22, font=("Arial", 10))
height_entry.grid(row=3, column=1, padx=(0,20), pady=6)

#Buttons
btn_frame= tk.Frame(root, bg="#F4F7FC")
btn_frame.grid(row=4, column=0, columnspan=2, pady=14)

tk.Button(btn_frame, text="Calculate BMI", command=calculate_bmi,
          bg="#0D2252", fg="black", font=("Arial", 10, 'bold'), pady=16, padx=6
          ).pack(side="left", padx=6)
tk.Button(btn_frame, text="Clear", command=clear_fields,
          bg="#0D2252", fg="black", font=("Arial", 10, 'bold'), pady=16, padx=6
          ).pack(side="left", padx=6)

result_label = tk.Label(root, text="Enter details and click calculate",
                        bg="#F4F7FC", fg="#4B5563",
                        font=("Arial", 11, 'bold')
                        )
result_label.grid(row=5, column=0, columnspan=2, pady=8)

root.mainloop()






#Change the result display so that instead of plain text, the result label background color changes to match the category — blue for Underweight, green for Normal, orange for Overweight, and red for Obese.
#Add a fourth field asking for the user's age — if the age is under 18, add a note to the result saying "Note: BMI works differently for children — consult a doctor."
#Display the ideal weight range for the user's height alongside the BMI result — calculate it using the normal BMI range (18.5 to 24.9) multiplied by height squared.
#Add input validation — if the user types letters instead of numbers in the weight or height fields, show a friendly error message in red instead of crashing.
#Add a history section at the bottom of the window that keeps a running list of the last 3 BMI results calculated, showing name and BMI value each time.
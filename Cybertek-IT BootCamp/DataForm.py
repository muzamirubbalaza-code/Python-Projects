import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def enter_data():
    accepted = accept_var.get()

    if accepted == "Accepted":
    #user info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        
        if firstname and lastname:
                title = title_combobox.get()
                age = age_spinbox.get()
                nationality = nationality_combobox.get()

                # Courses info
                registration_status = reg_status_var.get()
                numcourses = numcourses_spinbox.get()
                numsemesters = numsemesters_spinbox.get()

                print("First Name:",firstname,"Last Name:",lastname)
                print("Title:",title,"Age:",age,"Nationality:",nationality)
                print("# Courses:",numcourses,"# Semesters:",numsemesters)
                print("Registration Status:",registration_status)
                print("----------------------------------------------------")
        else:
                tk.messagebox.showwarning(title="Error ",message="First Name and Last Name are Required")        
    else:
            tk.messagebox.showwarning(title="Error",message="You Have Not Accepted the terms and conditions!")

window = tk.Tk()
window.title("Data Entry Form")

frame = tk.Frame(window)
frame.pack(padx=10,pady=10)

# Saving User Information
user_info_frame = tk.LabelFrame(frame,text="User Information")
user_info_frame.grid(row=0,column=0,padx=20,pady=10)


#Labels and Entries
first_name_label = tk.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0,column=0)

last_name_label = tk.Label(user_info_frame,text="Last Name")
last_name_label.grid(row=0,column=1)

first_name_entry = tk.Entry(user_info_frame)
last_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0,padx=5,pady=5)
last_name_entry.grid(row=1,column=1,padx=5,pady=5)


title_label = tk.Label(user_info_frame,text="title")
title_combobox =  ttk.Combobox(user_info_frame,values=["","Mr.","Ms.","Dr."])
title_label.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)


age_label = tk.Label(user_info_frame,text="Age")
age_spinbox = tk.Spinbox(user_info_frame,from_=18,to=110)
age_label.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)


nationality_label = tk.Label(user_info_frame,text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame,values=["Africa","Antarctica","Europe","Asia","North America","South America","Australia"])
nationality_label.grid(row=2,column=1)
nationality_combobox.grid(row=3,column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

#Saving course_information
courses_frame = tk.LabelFrame(frame)
courses_frame.grid(row=1,column=0,sticky="news",padx=20,pady=10)

registered_label = tk.Label(courses_frame,text="Registration Status")

reg_status_var = tk.StringVar(value="Not Registered")
registered_check = tk.Checkbutton(courses_frame,text="currently-registered",
                                 variable=reg_status_var,onvalue="Registered",offvalue="Not Registered")

registered_label.grid(row=0,column=0)
registered_check.grid(row=1,column=0)


numcourses_label = tk.Label(courses_frame,text="# Completed Courses")
numcourses_spinbox = tk.Spinbox(courses_frame,from_=0,to="infinity")
numcourses_label.grid(row=0,column=1)
numcourses_spinbox.grid(row=1,column=1)

numsemesters_label = tk.Label(courses_frame,text="# Semesters")
numsemesters_spinbox = tk.Spinbox(courses_frame,from_=0,to="infinity")
numsemesters_label.grid(row=0,column=2)
numsemesters_spinbox.grid(row=1,column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)


# Accept Terms
terms_frame = tk.LabelFrame(frame,text="Terms & Conditions")

accept_var = tk.StringVar(value="Not Accepted")
terms_check = tk.Checkbutton(terms_frame,text="I Accept the terms and Conditions.",
                             variable=accept_var,onvalue="Accepted",offvalue="Not Accepted")

terms_frame.grid(row=2,column=0,sticky="news",padx=20,pady=10)
terms_check.grid(row=0,column=0)

#Button
button = tk.Button(frame,text="Enter Data" ,command=enter_data)
button.grid(row=3,column=0,sticky="news",padx=20,pady=20)

# Run App
window.mainloop()
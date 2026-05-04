def happy_birthday(name,age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} Now!")
    print("Happy birthaday to you Dear!")
    print()
happy_birthday("Muzamiru",22)

def display_invoice(username,amount,due_date):
    print(f"Hello , {username}")
    print(f"Your Bill of ${amount: .2f} is due {due_date}")

display_invoice("Muzamiru",256.67,"5/4/2026")


# Return Statement: It is a statement that is used to end the function and send the result back to the user

def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("bbalaza","muzamiru")

print(full_name)
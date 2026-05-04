#String Methods: Text Manipulation
#Notation: string.method()
#Method 1 > len(s) : count characters including space

name = "muzamiru"
comment = 'WELCOME TO OUR CYBERTEKS-IT BOOTCAMP'
print(len(name))

#Method 2 > upper() :It changes a lowercase string into uppercase
print(name.upper())

#Method 3 > lower() : It changes a uppercase string into a lowercase
print(name.lower())

#method 4 > strip() : It removes the trailing spaces "caleb " > "caleb"
print(name.strip())

#Method 5 > replace() : It replaces a string in a sentence
print(comment.replace("OUR", "SECURE"))

#Method 6 > split() : It divides the strings
print(comment.split(" "))

#Method 7 startwith() : If the input is equals to the first characters , it gives true
print(comment.startswith("WELCOME"))

#Method 8 > endwith() : If the input is equals to the last characters , it gives true
print(comment.endswith("BOOTCAMP"))

#Method 9 > count(x) : It gives how many times x is found in the chosen string
print(comment.count('E'))

#Method 10 > find(x) : 











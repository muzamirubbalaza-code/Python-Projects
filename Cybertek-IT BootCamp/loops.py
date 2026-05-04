#Loops : They are used for repeating actions , to repeat a block of code automatically
#For loop : When the programmer knows how many lines to pepeat in the code
#for b in range(1,11,2):
  #  print("iteration:",b)

#for x in "banana":
#  print(x)
#print("==================")
# While Loop: Used when we repeat until the condition becomes false
#i = 1
#while i < 6:
 # print(i)
 # i += 1

  
 # password=""
 # while password != "cyberteks2026":
 #   password = input("Enter the right Password:") 
 # print("Access Granted!")

 # Q1.  Use a for loop to print the multiplication table of any number entered by the user (1× to 12×).
#Hint: Use range(1, 13) and multiply the user's number by i
#Q2.  Write a while loop that asks the user to guess a secret number (e.g. 7). Keep looping until they get it right.
#Hint: while guess != secret: keep asking
#Q3.  Use a for loop with range() to print all even numbers from 2 to 20.
#Hint: Use range(2, 21, 2) or check i % 2 == 0
#Q4.  BONUS — Use a for loop to count down from 10 to 1, then print 'Launch! 🚀'
#Hint: range(10, 0, -1) counts down. Print after loop ends.


#Q1.
#number = int(input("Enter a Number:"))

#for i in range(1,13):
 # print(number, "x", i, "=", number * i)

#for x in reversed(range(1,11)):
 #   print(x)

#print("HAPPY NEW YEAR")

#for x in range(1,21):
 #   if x == 13:
 #     break #continue
 #   else:
 #      print(x)

name = input("Enter Your Name: ")

if name == "":
    print("You didnot Enter Your Name")
else:
    print(f"Hello , {name}")


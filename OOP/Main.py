# Object Oriented Programming (OOP) in Python
# Class: A blueprint for creating objects (a particular data structure)
class Person:
   def __init__(self,name,age):
       self.name = name
       self.age = age
   
   def greet(self):
        print("Hello, my name is", self.name)





# Create an object
p1 = Person("Muzamiru",22)
# Call the greet method
p1.greet()
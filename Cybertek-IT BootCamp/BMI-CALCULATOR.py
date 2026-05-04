# Under weight: below 18.5, Normal weight18.5-24.9, OverWeight:25.0-29.9, Obese:30.0 an above
# BMI = weight (kg) / height (m)^2
# Tips

# Personal Details
name = input("What's your name: ")
age = input("What's your age: ")
weight = float(input("What's your weight: "))
height = float(input("What's your height: "))

#Bmi Calculation
bmi=weight/(height**2)

# Categories

if bmi<18.5:
    category="underweight"
    comment="You need to eat moore calories..."
elif 25.0 > bmi >= 18.5:
    category="normal"
    comment="You are on a normal track..."
elif 29.9 > bmi >= 25.0:
    category="overweight"
    comment="You need to start a diet..."
else:
    category="Obese"
    comment="You need to see a health professional..."

print("==============================")
print("BMI Calculator")
print("==============================")
print("Calories are units of energy that measure how much energy your \n body gets from food and drinks, \n as well as how much it burns to function")
print("==============================")
print("Personal Details")
print("==============================")
print("Name:     ", name)
print("Age:      ", age)
print("Weight:   ", weight, "kg")
print("Height:   ", height, "meters")
print("BMI:      ", bmi)
print("Category: ", category)
print("Comments: ", comment)
print("==============================")
print("Thank you for checking your health status with My BMI Calculator")
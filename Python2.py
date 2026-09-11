#  task 1 Program to print your full name
print("Sowjanya Ramesh")

#  task 2 Printing a welcome message on multiple lines
print("\nTASK2")
print("Welcome to Python Programming!")
print("This is your learning journey.")
print("Let's explore coding together.")

#  task 3 Taking input from user
print("\n TASK3")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
favorite_color = input("Enter your favorite color: ")

print("Name:", name)
print("Age:", age)
print("Favorite Color:", favorite_color)

# task 4 Defining variables of different data types
print("\nTASK4")
name = "Sowjanya"        
age = 25                 
height = 5.6             
is_student = True        
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Is Student:", is_student, "| Type:", type(is_student))

#  task 5 Taking user input and printing a welcome message
print("\nTASK5")
name = input("Enter your name: ")
print("Welcome to Python Programming,", name + "!")

# task 6 Program to add two numbers
print("\nTASK6")
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num1 = int(num1)
num2 = int(num2)
sum_result = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum_result)

#  task 7 Program to demonstrate data type conversion
print("\nTASK7")
num = input("Enter a number: ")
print("Before conversion:", num, "| Type:", type(num))
num = float(num)
print("After conversion:", num, "| Type:", type(num))

# task 8 Program to display a formatted sentence using f-string
print("\nTASK8")
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
print(f"Hello, my name is {name}. I am {age} years old and I live in {city}.")

# task 9 Program to calculate the area of a rectangle
print("\nTASK9")
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle with length {length} and width {width} is {area}.")

#task 10 Program to print a receipt using f-strings
print("\nTASK10")
item = input("Enter the item name: ")
quantity = int(input("Enter the quantity: "))
price = float(input("Enter the price per item: "))
total = quantity * price
print("\n===== Store Receipt =====")
print(f"Item: {item}")
print(f"Quantity: {quantity}")
print(f"Price per item: ₹{price:.2f}")
print(f"Total: ₹{total:.2f}")
print("=========================")

# task 11 Program to swap two numbers without a third variable
print("\nTASK11")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"Before swapping: a = {a}, b = {b}")
a = a + b
b = a - b
a = a - b
print(f"After swapping: a = {a}, b = {b}")

#  task 12 Program to convert Celsius to Fahrenheit
print("\nTASK12")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

# task 13 Program to display a simple profile
print("\nTASK13")
name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height (in cm): ")
hobby = input("Enter your favorite hobby: ")
print("\n===== User Profile =====")
print(f"Name   : {name}")
print(f"Age    : {age}")
print(f"Height : {height} cm")
print(f"Hobby  : {hobby}")
print("========================")

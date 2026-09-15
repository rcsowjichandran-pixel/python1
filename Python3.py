# Task 1 Program to perform arithmetic operations on two numbers

# Taking input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Performing operations
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")

# Handling division safely
if num2 != 0:
    print(f"Quotient: {num1 / num2}")
    print(f"Remainder: {num1 % num2}")
else:
    print("Division and remainder cannot be calculated (division by zero).")


# TASK 2 Program to compare two numbers

# Taking input from the user
print("TASK2")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Comparing the numbers
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")


# TASK 3 Program to swap two numbers using arithmetic operators

# Taking input from the user
print("TASK3")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(f"Before swapping: a = {a}, b = {b}")

# 🔹 Method 1: Using Addition and Subtraction
a = a + b
b = a - b
a = a - b
print(f"After swapping (Addition/Subtraction): a = {a}, b = {b}")

# Resetting values for second method
a = int(input("\nEnter the first number again: "))
b = int(input("Enter the second number again: "))

print(f"Before swapping: a = {a}, b = {b}")

# 🔹 Method 2: Using Multiplication and Division
a = a * b
b = a / b   # quotient gives original 'a'
a = a / b   # quotient gives original 'b'
print(f"After swapping (Multiplication/Division): a = {int(a)}, b = {int(b)}")


# TASK 4 Program to check if a year is a leap year using modulus operator
print("TASK4")
year = int(input("Enter a year: "))

# Leap year conditions:
# 1. Divisible by 4
# 2. Not divisible by 100, unless also divisible by 400

if (year % 400 == 0):
    print(f"{year} is a leap year")
elif (year % 100 == 0):
    print(f"{year} is not a leap year")
elif (year % 4 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# TASK 5 Program to find the largest of three numbers

# Taking input from the user
print("TASK5")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Comparing the numbers
if num1 >= num2 and num1 >= num3:
    print(f"The largest number is {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is {num2}")
else:
    print(f"The largest number is {num3}")


# TASK 6 Program to calculate the area of a circle

# Taking radius as input
print("TASK6")
radius = float(input("Enter the radius of the circle: "))

# Using 3.14 for π
pi = 3.14
area = pi * radius ** 2

# Displaying the result
print(f"The area of the circle with radius {radius} is {area}")

#  TASK 7 Program to check if a number is positive, negative, or zero

# Taking input from the user
print("TASK7")
num = float(input("Enter a number: "))

# Checking conditions
if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print("The number is zero")


# TASK 8 Program to check voting eligibility

# Taking age as input
print("TASK8")
age = int(input("Enter your age: "))

# Checking eligibility
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# TASK 9 Program to assign grades based on marks

# Taking marks as input
print("TASK9")
marks = int(input("Enter your marks: "))

# Checking grade conditions
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: Fail")


# TASK 10 Simple ATM Withdrawal Program

# Initial account balance
print("TASK10")
balance = 5000

# Ask the user for withdrawal amount
withdraw = int(input("Enter the amount you want to withdraw: "))

# Check if withdrawal is possible
if withdraw > balance:
    print("Insufficient funds.")
else:
    balance -= withdraw
    print(f"Withdrawal successful! Remaining balance: {balance}")


# TASK 11 Program to check divisibility by 5 and 11

# Taking input from the user
print("TASK11")
num = int(input("Enter a number: "))

# Checking divisibility
if num % 5 == 0 and num % 11 == 0:
    print(f"{num} is divisible by both 5 and 11")
else:
    print(f"{num} is not divisible by both 5 and 11")


# TASK 12 Program to check if a character is a vowel or consonant

# Taking single character input
print("TASK12")
ch = input("Enter a single character: ")

# Ensuring only one character is entered
if len(ch) != 1 or not ch.isalpha():
    print("Please enter a single alphabet character.")
else:
    # Checking for vowels
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(f"{ch} is a vowel")
    else:
        print(f"{ch} is a consonant")


# TASK 13 Program to check if a number is even or odd using ternary operator
print("TASK13")
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")
       

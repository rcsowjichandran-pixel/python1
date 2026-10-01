# print("\n TASK 1")
# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

# # Object creation
# my_car = Car("Toyota", "Corolla", 2022)

# # Print details
# print("Brand:", my_car.brand)
# print("Model:", my_car.model)
# print("Year:", my_car.year)

# print("\n TASK 2")
# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def start_engine(self):
#         print("Engine started!")

# # Object creation
# my_car = Car("Honda", "Civic", 2023)

# # Call method
# my_car.start_engine()


# print("\n TASK 3")
# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def display(self):
#         print(f"{self.year} {self.brand} {self.model}")

# # Multiple objects
# car1 = Car("Toyota", "Corolla", 2022)
# car2 = Car("Honda", "Civic", 2023)

# car1.display()
# car2.display()


# print("\n TASK 4")
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.__balance = balance   # private variable

#     def deposit(self, amount):
#         self.__balance += amount
#         print(f"Deposited {amount}")

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew {amount}")
#         else:
#             print("Insufficient balance!")

#     def check_balance(self):
#         print(f"Balance: {self.__balance}")

# # Demo
# acc = BankAccount("Sowjanya", 1000)
# acc.deposit(500)
# acc.withdraw(300)
# acc.check_balance()

# print("\n TASK 5")
# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def show_details(self):
#         print(f"Vehicle: {self.brand} {self.model}")

# class Car(Vehicle):
#     def __init__(self, brand, model, seats):
#         super().__init__(brand, model)
#         self.seats = seats

# # Demo
# c = Car("Hyundai", "i20", 5)
# c.show_details()


# print("\n TASK 6")
# class Car(Vehicle):
#     def __init__(self, brand, model, seats):
#         super().__init__(brand, model)
#         self.seats = seats

#     def show_details(self):   # overriding
#         print(f"Car: {self.brand} {self.model}, Seats: {self.seats}")

# c = Car("Hyundai", "i20", 5)
# c.show_details()

# print("\n TASK 7")
# class Teacher:
#     def work(self):
#         print("Teaching students")

# class Researcher:
#     def work(self):
#         print("Doing research")

# class Professor(Teacher, Researcher):
#     def work(self):
#         print("Teaching and researching")

# # Demo
# p = Professor()
# p.work()

# print("\n TASK 8")
# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# # Demo
# c = Circle(5)
# r = Rectangle(4, 6)
# print("Circle area:", c.area())
# print("Rectangle area:", r.area())


# print("\n TASK 9")
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         return f"({self.x}, {self.y})"

# # Demo
# v1 = Vector(2, 3)
# v2 = Vector(4, 5)
# v3 = v1 + v2
# print("Resultant Vector:", v3)


# print("\n TASK 10")
# class Person:
#     count = 0   # class variable

#     def __init__(self, name):
#         self.name = name
#         Person.count += 1

#     @classmethod
#     def count_people(cls):
#         print(f"Total people created: {cls.count}")

#     @staticmethod
#     def greet():
#         print("Hello! Welcome to the Person class.")

# # Demo
# p1 = Person("Sowjanya")
# p2 = Person("Arun")
# Person.count_people()
# Person.greet()

# print("\n TASK 11")
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount
#         self.save_transaction(f"Deposited {amount}")

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             self.save_transaction(f"Withdrew {amount}")
#         else:
#             self.save_transaction("Failed withdrawal: Insufficient balance")

#     def check_balance(self):
#         return self.__balance

#     def save_transaction(self, message):
#         with open("transactions.txt", "a") as file:
#             file.write(f"{self.owner}: {message}\n")

#     def read_transactions(self):
#         with open("transactions.txt", "r") as file:
#             print(file.read())

# # Demo
# acc = BankAccount("Sowjanya", 1000)
# acc.deposit(500)
# acc.withdraw(200)
# acc.read_transactions()

# print("\n TASK 12")
# class Student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

#     def update_marks(self, new_marks):
#         self.marks = new_marks

#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")

# # Demo
# s1 = Student("Sowjanya", 20, 85)
# s1.display()
# s1.update_marks(90)
# s1.display()

# print("\n TASK 13")
# class Employee:
#     def __init__(self, name, emp_id, salary):
#         self.name = name
#         self.emp_id = emp_id
#         self.salary = salary

#     def calculate_salary(self):
#         tax = self.salary * 0.1   # 10% tax
#         return self.salary - tax

#     def give_raise(self, amount):
#         self.salary += amount

#     def save_details(self):
#         with open("employees.txt", "a") as file:
#             file.write(f"{self.emp_id}, {self.name}, Salary: {self.salary}\n")

# # Demo
# e1 = Employee("Sowjanya", 101, 50000)
# print("Salary after tax:", e1.calculate_salary())
# e1.give_raise(5000)
# e1.save_details()

# print("\n TASK 14")
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     return a / b

# print("\n TASk 15")
# import math

# num = 5
# print("Square root:", math.sqrt(num))       # 2.236...
# print("Factorial:", math.factorial(num))    # 120
# print("Power:", math.pow(2, 3))             # 8.0

# print("\n TASK 16")
# from random import randint, shuffle, choice

# # Generate random number between 1 and 100
# print("Random number:", randint(1, 100))

# # Shuffle a list
# numbers = [1, 2, 3, 4, 5]
# shuffle(numbers)
# print("Shuffled list:", numbers)

# # Choose a random item from a list
# fruits = ["Apple", "Banana", "Mango", "Orange"]
# print("Random fruit:", choice(fruits))


# print("\n TASK 17")
# import datetime

# # Current date and time
# now = datetime.datetime.now()
# print("Current Date & Time:", now)

# # Current date
# print("Date:", now.date())

# # Current time
# print("Time:", now.time())

# # Day of the week
# print("Day of Week:", now.strftime("%A"))


# print("\n TASk 18")
# import os

# # Current working directory
# print("Current Directory:", os.getcwd())

# # List files in current directory
# print("Files:", os.listdir("."))

# # Create a new folder
# new_folder = "my_folder"
# if not os.path.exists(new_folder):
#     os.mkdir(new_folder)
#     print(f"Folder '{new_folder}' created!")
# else:
#     print(f"Folder '{new_folder}' already exists.")


# print("\n TASK 19")
# def reverse_string(s):
#     return s[::-1]

# def to_uppercase(s):
#     return s.upper()

# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     return sum(1 for char in s if char in vowels)


# print("\n TASK 20")
# import sys

# print("Command-line arguments:")
# for arg in sys.argv:
#     print(arg)

# print("\n TASK 21")
# import time

# def sample_function():
#     total = 0
#     for i in range(1, 1000000):
#         total += i
#     return total

# start = time.time()
# result = sample_function()
# end = time.time()

# print("Result:", result)
# print("Execution time:", end - start, "seconds")

# print("\n TASk 22")
# students = {}

# def add_student(name, age, marks):
#     students[name] = {"age": age, "marks": marks}

# def remove_student(name):
#     if name in students:
#         del students[name]

# def display_students():
#     for name, details in students.items():
#         print(f"Name: {name}, Age: {details['age']}, Marks: {details['marks']}")


# print("\n TASK 23")
# import calendar

# year = int(input("Enter year: "))
# month = int(input("Enter month: "))

# print(calendar.month(year, month))


# print("\n TASK 24")
# import json

# data = {"name": "Sowjanya", "age": 25, "city": "Karur"}

# # Save to file
# with open("data.json", "w") as file:
#     json.dump(data, file)

# # Read back
# with open("data.json", "r") as file:
#     loaded_data = json.load(file)

# print("Loaded JSON:", loaded_data)


print("\n TASK 25")
def write_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

def read_file(filename):
    with open(filename, "r") as file:
        return file.read()

def append_file(filename, content):
    with open(filename, "a") as file:
        file.write(content)

# print("\n TASK 26")
# # import requests

# # # Example: OpenWeatherMap API (replace YOUR_API_KEY with actual key)
# # url = "https://api.openweathermap.org/data/2.5/weather?q=Karur&appid=YOUR_API_KEY&units=metric"

# # response = requests.get(url)
# # data = response.json()

# # print("City:", data["name"])
# # print("Temperature:", data["main"]["temp"], "°C")
# # print("Weather:", data["weather"][0]["description"])


# import requests

# url = "https://api.openweathermap.org/data/2.5/weather?q=Karur&appid=YOUR_API_KEY&units=metric"
# response = requests.get(url)
# data = response.json()

# if "name" in data:
#     print("City:", data["name"])
#     print("Temperature:", data["main"]["temp"], "°C")
#     print("Weather:", data["weather"][0]["description"])
# else:
#     print("Error:", data)

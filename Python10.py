print("\n TASK 1")
with open("data.txt", "w") as f:
    f.write("Hello, File Handling!")

print("\n TASK 2")
with open("data.txt", "r") as f:
    print(f.read())

print("\n TASK 3")
with open("data.txt", "a") as f:
    f.write("\nThis is a new line.")

print("\n TASK 4")
with open("data.txt", "r") as f:
    content = f.read()
    words = content.split()
    print("Word count:", len(words))

print("\n TASK 5")
with open("data.txt", "r") as src, open("copy.txt", "w") as dest:
    dest.write(src.read())

# Verify by reading copy.txt
with open("copy.txt", "r") as f:
    print(f.read())
    
# print("\n TASK 5")
# with open("data.txt", "r") as src, open("copy.txt", "w") as dest:
#     dest.write(src.read())

print("\n TASK 6")
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())

print("\n TASK 7")
word = input("Enter a word to search: ")
with open("data.txt", "r") as f:
    content = f.read()
    if word in content:
        print(f"'{word}' found in file.")
    else:
        print(f"'{word}' not found.")

print("\n TASK 8")
with open("data.txt", "r") as f:
    content = f.read()

content = content.replace("old", "new")

with open("data.txt", "w") as f:
    f.write(content)

print("\n TASK 9")
names = ["Sowjanya", "Arun", "Meena"]

# Store
with open("names.txt", "w") as f:
    for name in names:
        f.write(name + "\n")

# Retrieve
with open("names.txt", "r") as f:
    print("Names:", f.read().splitlines())

# print("\n TASK 10")
with open("data.txt", "r") as f:
    lines = f.readlines()
    print("Line count:", len(lines))

print("\n TASK 11")
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged.txt", "w") as merged:
    merged.write(f1.read() + "\n" + f2.read())

print("\n TASK 12")
import csv

# Create CSV
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Score"])
    writer.writerow(["Sowjanya", 95])
    writer.writerow(["Arun", 88])
    writer.writerow(["Meena", 92])

# Read CSV
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("\n TASK 13")
with open("data.txt", "r") as f:
    lines = f.readlines()

cleaned = [line for line in lines if line.strip() != ""]

with open("cleaned.txt", "w") as f:
    f.writelines(cleaned)

print("Blank lines removed and saved to cleaned.txt")

print("\n TASK 14")
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

print("\n TASK 15")
try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)
except ValueError:
    print("Error: Please enter a valid number!")

print("\n TASK 16")
my_list = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index (0–4): "))
    print("Value:", my_list[index])
except IndexError:
    print("Error: Index out of range!")

print("\n TASK 17")
students = {"Sowjanya": 95, "Arun": 88, "Meena": 92}

try:
    name = input("Enter student name: ")
    print("Marks:", students[name])
except KeyError:
    print("Error: Student not found!")

print("\n TASK 18")
try:
    filename = input("Enter filename: ")
    with open(filename, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File does not exist!")

print("\n TASK 19")
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input, enter a number!")

print("\n TASK 20")
class NegativeNumberError(Exception):
    pass

def check_number(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    else:
        print("Number is valid:", n)

try:
    num = int(input("Enter a number: "))
    check_number(num)
except NegativeNumberError as e:
    print(e)

print("\n TASK 21")
class OddNumberError(Exception):
    pass

try:
    num = int(input("Enter a number: "))
    if num % 2 != 0:
        raise OddNumberError("Odd numbers are not allowed!")
    else:
        print("Even number entered:", num)
except OddNumberError as e:
    print(e)

print("\n TASK 22")
class InsufficientBalanceError(Exception):
    pass

balance = 1000  # Example balance

try:
    amount = int(input("Enter withdrawal amount: "))
    if amount <= 0:
        raise ValueError("Invalid withdrawal amount!")
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance!")
    balance -= amount
    print("Withdrawal successful! Remaining balance:", balance)
except ValueError as e:
    print("Error:", e)
except InsufficientBalanceError as e:
    print("Error:", e)


print("\n TASK 23")
class InvalidMarksError(Exception):
    pass

try:
    marks = int(input("Enter student marks (0–100): "))
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100!")
    print("Marks entered:", marks)
except InvalidMarksError as e:
    print("Error:", e)
except ValueError:
    print("Error: Please enter a valid number!")

print("\n TASK 24")
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2

    with open("result.txt", "w") as f:
        f.write(f"Result: {result}")
    print("Result saved to result.txt")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input, please enter numbers!")
except FileNotFoundError:
    print("Error: File not found!")

print("\n TASK 25")
class InvalidUsernameError(Exception):
    pass

class ShortPasswordError(Exception):
    pass

try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != "admin":
        raise InvalidUsernameError("Invalid username!")
    if len(password) < 5:
        raise ShortPasswordError("Password too short!")

    print("Login successful!")

except InvalidUsernameError as e:
    print("Error:", e)
except ShortPasswordError as e:
    print("Error:", e)

print("\n TASK 26")
import logging

# Configure logging
logging.basicConfig(filename="errors.log", level=logging.ERROR)

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)
except Exception as e:
    logging.error("Error occurred: %s", e)
    print("An error occurred. Check errors.log for details.")

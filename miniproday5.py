from functools import reduce

# 1. Function to calculate average score
def calculate_average(*args):
    return sum(args) / len(args) if args else 0

# 2. Convert marks into grades using map + lambda
def marks_to_grades(marks):
    return list(map(lambda m: "A" if m >= 90 else 
                              "B" if m >= 80 else 
                              "C" if m >= 70 else 
                              "F", marks))

# 3. Filter students who passed (grade != "F")
def passed_students(students):
    return list(filter(lambda s: s["grade"] != "F", students))

# 4. Use reduce() to find highest score among all students
def highest_score(students):
    return reduce(lambda a, b: a if a > b else b, [s["score"] for s in students])

# 5. Recursion to print first n students' details
def print_students_recursive(students, n):
    if n == 0:
        return
    student = students[n-1]
    print(f"Student: {student['name']}, Age: {student['age']}, Average Score: {student['score']}, Grade: {student['grade']}")
    print_students_recursive(students, n-1)

# 6. Store student details dynamically using **kwargs
def create_student(**kwargs):
    return kwargs

# ------------------ DEMO ------------------

# Create students
student1 = create_student(name="John", age=16, score=85, grade="B")
student2 = create_student(name="Emily", age=17, score=95, grade="A")
student3 = create_student(name="Mike", age=16, score=65, grade="F")

students = [student1, student2, student3]

# Print student details recursively (first 2 students)
print_students_recursive(students, 2)

# Find passed students
passed = passed_students(students)
print("Passed Students:", [s["name"] for s in passed])

# Find highest score
print("Highest Score:", highest_score(students))



print("\n MINIPRO 2")
from functools import reduce

# Global variable to track total transactions
total_transactions = 0

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        global total_transactions
        self.balance += amount
        total_transactions += 1
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        global total_transactions

        # Inner function to check withdrawal possibility
        def can_withdraw():
            return self.balance >= amount

        if can_withdraw():
            # Transaction fee using lambda
            fee = (lambda amt: amt * 0.02)(amount)
            self.balance -= (amount + fee)
            total_transactions += 1
            print(f"Withdrawn: {amount}, Transaction Fee: {fee}")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.balance

# First-class function: apply interest rate
def apply_interest(account, interest_func):
    account.balance = interest_func(account.balance)
    print(f"Balance after interest: {account.balance}")

# ---------------- DEMO ----------------
account = BankAccount("Alice", 0)

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(200)

# Check balance
print("Balance:", account.get_balance())

# Apply interest (5%)
apply_interest(account, lambda bal: bal * 1.05)

# Show global transactions
print("Total Transactions:", total_transactions)

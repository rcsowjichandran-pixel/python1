# 1. Function to greet user
print("\n TASK 1")
def greet_user():
    print("Hello, User!")
greet_user()

# 2. Function to calculate sum
print("\n TASK 2")
def calculate_sum(a, b):
    return a + b
result = calculate_sum(7, 5)
print("The sum is:", result)

# 3. Function to check if number is positive
print("\n TASK 3")
def check_positive(num):
    if num > 0:
        return "Positive"
    else:
        pass 
print(check_positive(10))   
print(check_positive(-5))  
print(check_positive(0)) 

# 4. Function to find maximum of three numbers
print("\n TASK 4")
def find_max(a, b, c):
    return max(a, b, c)
print(find_max(10, 25, 7))   
print(find_max(-3, -8, -1)) 

# 5. Demonstrating global vs local variables
print("\n TASK 5")
count = 10  # Global variable

def modify_global():
    global count
    count += 5  # Modifies global variable
print("Inside function, count =", count)
print("Before function call, count =", count)
modify_global()
print("After function call, count =", count)

# 6. Local variable scope demonstration
print("\n TASK 6")
def modify_variable():
    message = "Local Scope"
    print("Inside function:", message)
modify_variable()

# Trying to access 'message' outside the function
try:
    print("Outside function:", message)
except NameError as e:
    print("Outside function error:", e)

# 7. Recursive factorial function
print("\n TASK 7")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))   
print(factorial(0))   


# 8. Recursive Fibonacci function
print("\n TASK 8")
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(0))   
print(fibonacci(1))   
print(fibonacci(6))  

# 9. Function with *args to sum numbers
print("\n TASK 9")
def sum_numbers(*args):
    return sum(args)
print(sum_numbers(1, 2, 3, 4, 5))
print(sum_numbers(10, 20))          
print(sum_numbers()) 

# 10. Function with **kwargs to print student details
print("\n TASK 10")
def print_student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_student_details(name="Alice", age=20, grade="A")
print_student_details(name="Sowjanya", age=22, grade="B+", subject="Math")

# 11. Function that applies an operation
print("\n TASK 11")
def apply_operation(func, a, b):
    return func(a, b)

result = apply_operation(lambda x, y: x + y, 4, 6)
print("Result:", result)

# 12. Function with inner function
print("\n TASK 12")
def outer_function():
    def inner():
        return "Hello from Inner Function"
    return inner()
print(outer_function())

# 13. Using map() to double elements
print("\n TASK 13")
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

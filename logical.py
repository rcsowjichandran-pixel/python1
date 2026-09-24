text=input("Enter a string:")
reversed_text=""
for char in text:
    reversed_text=char+reversed_text
print("Reversed string:",reversed_text) 
# using while loop
text="Sowjanya"
reversed_text=""
i=len(text)-1
while i>=0:
    reversed_text +=text[i]
    i-=1
print("Reversed string:", reversed_text)

print("\n TASK 2")
num=int(input("Enter a number:"))
if num%2==0:
    print(f"{num} is Even")
else:
    print(f"{num} is odd")

print("\n TASK 3")
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
num3 = float(input("Enter the third number:"))
if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest number.")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the largest number.")
else:
    print(f"{num3} is the largest number.")
# shorter method
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
num3 = float(input("Enter the third number:"))
print("The largest number is",max(num1,num2,num3))

print("\n TASK 4")
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
num3=float(input("Enter the third number:"))
if num1<=num2 and num1<=num3:
    print(f"{num1} is the smallest number.")
elif num2<=num1 and num2<=num3:
    print(f"{num2} is the smallest number.")
else:
    print(f"{num3} is the smallest number.")
# Shorter method
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
num3=float(input("Enter the third number:"))
print("The smallest number is",min(num1,num2,num3))

print("\nTASK 5")
numbers=[12,45,7,89,34]
largest=numbers[0]
for num in numbers:
    if num>largest:
        largest=num
print("The largest number in the list is:",largest)
# shorter method
numers=[12,45,7,89,34]
largest=sorted(numbers)[-1]
print("The largest number in the list is:",largest)

print("\n TASK 6")
numbers=[12,45,7,89,34]
smallest=numbers[0]
for num in numbers:
    if num<smallest:
        smallest=num
print("The largest number in the list is:",smallest)
# shorter method
numers=[12,45,7,89,34]
smallest=sorted(numbers)[0]
print("The largest number in the list is:",smallest)


print("\n TASK 7")
numbers=[12,45,90,7,56,67]
unique_numbers=list(set(numbers))
unique_numbers.sort()
second_largest=unique_numbers[-2]
print("The second largest number in the list is:",second_largest)
# using logic 
numbers = [12, 45, 7, 89, 34, 67]
largest = second = float('-inf')
for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print("The second largest number in the list is:", second)

print("\n TASK 8")
numbers=[12,45,90,7,56,67]
unique_numbers=list(set(numbers))
unique_numbers.sort()
second_smallest=unique_numbers[1]
print("The second smallest number in the list is:",second_smallest)
# using logic 
numbers = [12, 45, 7, 89, 34, 67]
smallest = second = float('inf')
for num in numbers:
    if num < smallest:
        second = smallest
        smallest = num
    elif num < second and num != smallest:
        second = num
print("The second smallest number in the list is:", second)

print("\n TASK 9")
numbers=[12,45,7,89,12,34,45,7]
unique_numbers=list(set(numbers))
print("List after removing duplicates(unordered):",unique_numbers)
# original order
unique_ordered=[]
for num in numbers:
    if num not in unique_ordered:
        unique_ordered.append(num)
print("List after removing duplicates(ordered):",unique_ordered)

print("\n TASK 10")
numbers=[12,45,7,89,34,45,12,7]
duplicates=[]
for num in numbers:
    if numbers.count(num)>1 and num not in duplicates:
        duplicates.append(num)
print("Duplicate elements in the list are:",duplicates)
# Efficient Method
numbers = [12, 45, 7, 89, 34, 45, 12, 7, 89, 100]
seen = set()
duplicates = set()
for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
print("Duplicate elements in the list are:", list(duplicates))

print("\n TASK 11")

numbers = [10, 20, 10, 30, 20, 40, 10, 30, 50]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1   # increment count if already present
    else:
        frequency[num] = 1    # add new entry with count 1
print("Frequency of each element:")
for key, value in frequency.items():
    print(f"{key} -> {value}")
Another Method
from collections import Counter

numbers = [10, 20, 10, 30, 20, 40, 10, 30, 50]
frequency = Counter(numbers)

print("Frequency of each element:", dict(frequency))


print("\n TASK 12")
# Program to count frequency of each character in a string
text = "banana"
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] += 1   # increment count if already present
    else:
        frequency[char] = 1    # add new entry with count 1
print("Character Frequency:")
for key, value in frequency.items():
    print(f"'{key}' -> {value}")
Another Method
from collections import Counter
text = "banana"
frequency = Counter(text)
print("Character Frequency:", dict(frequency))


print("\n TASK 13")
# Program to check if a string is a palindrome
text = input("Enter a string: ")
text = text.lower()
if text == text[::-1]:
    print("The string is a palindrome ✅")
else:
    print("The string is not a palindrome ❌")

print("\n TASK 14")
# Program to check if a number is a palindrome
num = int(input("Enter a number: "))
num_str = str(num)
if num_str == num_str[::-1]:
    print(f"{num} is a palindrome ✅")
else:
    print(f"{num} is not a palindrome ❌")

print("\n TASK 15")
# Program to check if a number is prime
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:
            print(f"{num} is not a prime number ❌")
            break
    else:
        print(f"{num} is a prime number ✅")
else:
    print(f"{num} is not a prime number ❌")

print("\n TASK 16")
# Program to print all prime numbers between 1 and 100
for num in range(2, 101): 
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

print("\n TASK 17")
# Program to find the factorial of a number
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers ❌")
elif num == 0 or num == 1:
    print(f"Factorial of {num} is 1 ✅")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial} ✅")

print("\n TASK 18")
# Program to generate Fibonacci series
n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b   

print("\n TASK 19")
# Program to find the sum of digits of a number
num = int(input("Enter a number: "))
digit_sum = 0
while num > 0:
    digit_sum += num % 10   
    num //= 10              
print("Sum of digits:", digit_sum)

print("\n TASK 20")
num = 1234
reversed_num = int(str(num)[::-1])
print("Reversed Number:", reversed_num)




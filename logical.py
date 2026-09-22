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
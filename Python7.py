print("\n TASK 1")
# Creating a tuple with five fruits
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")
print(fruits)
print("\n TASK 2")
# Tuple of fruits
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")
third_fruit = fruits[2]
print("Third fruit:", third_fruit)
print("Length of third fruit:", len(third_fruit))
print("\n TASK 3")
# Creating a tuple with 5 numbers
numbers = (10, 20, 30, 40, 50)
first_num = numbers[0]
last_num = numbers[-1]
print("First element:", first_num)
print("Last element:", last_num)
print("\n TASK 4")
# Tuple with numbers
numbers = (1, 2, 3, 4, 5)
names = ("Alice", "Bob", "Charlie")
combined = numbers + names
print("Combined tuple:", combined)
print("\n TASK 5")
# Creating a tuple of numbers from 1 to 10
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
slice_part = numbers[2:8]   
print("Sliced tuple:", slice_part)
print("\n TASK 6")
# Original tuple
fruits = ("Apple", "Banana", "Mango", "Orange")
fruits_list = list(fruits)
# Modify an element (change "Banana" to "Grapes")
fruits_list[1] = "Grapes"
modified_fruits = tuple(fruits_list)
print("Modified tuple:", modified_fruits)
print("\n TASk 7")
# Creating a tuple
numbers = (1, 2, 3, 4, 5)
print("Tuple before deletion:", numbers)
del numbers
# print("Tuple after deletion:", numbers)   # ❌ This will cause an error
print("\n tASK 8")
fruits = ("Apple", "Banana", "Mango", "Apple", "Orange", "Apple")
apple_count = fruits.count("Apple")
print("The fruit 'Apple' appears", apple_count, "times.")
print("\n TASK 9")
numbers = (5, 10, 15, 20, 25)
maximum = max(numbers)
minimum = min(numbers)
total = sum(numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Sum:", total)
print("\n TASK 10")
# Creating a tuple and a list with the same elements
my_tuple = (1, 2, 3, 4, 5)
my_list = [1, 2, 3, 4, 5]
try:
    my_tuple[0] = 10
except TypeError as e:
    print("Tuple Error:", e)
my_list[0] = 10
print("Modified list:", my_list)
print("\n TASK 11")
# Creating a tuple of numbers
numbers = (10, 20, 30, 40, 50)
check_num = 30
if check_num in numbers:
    print(check_num, "exists in the tuple.")
else:
    print(check_num, "does not exist in the tuple.")
print("\n TASK 12")
# Creating a tuple of four colors
colors = ("Red", "Green", "Blue", "Yellow")
c1, c2, c3, c4 = colors
print("Color 1:", c1)
print("Color 2:", c2)
print("Color 3:", c3)
print("Color 4:", c4)
print("\n TASk 13")
# Creating a tuple with names
names = ("Alice", "Bob", "Charlie", "David")
for name in names:
    print(name.upper())
print("\n TASK 14")
# Creating a list of 5 favorite movies
movies = ["Amaran", "Inspector Rishi", "The Dark Knight", "Officer on Duty", "Titanic"]
print("My favorite movies are:", movies)
print("\n TASK 15")
# Creating a list of numbers
numbers = [10, 20, 30, 40, 50]
second_element = numbers[1]
fourth_element = numbers[3]
print("Second element:", second_element)
print("Fourth element:", fourth_element)
print("\n TASK 16")
# Existing list of fruits
fruits = ["Apple", "Banana", "Mango"]
fruits.append("Orange")   
fruits.append("Grapes")   
fruits.insert(1, "Pineapple")   
print("Updated fruits list:", fruits)
print("\n TASK 17")
# Creating a list of books
books = ["Harry Potter", "The Hobbit", "Pride and Prejudice", "1984", "The Alchemist"]
books[2] = "To Kill a Mockingbird"
print("Updated book list:", books)
print("\n TASK 18")
# Creating a list of fruits
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
fruits.remove("Mango")
print("After .remove():", fruits)
del fruits[2]
print("After del:", fruits)
print("\n TASK 19")
# Creating a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:   
        print(num)
print("\n TASK 20")
# Creating a list of names
names = ["Alice", "Bob", "Charlie", "David", "Emma"]
for name in names:
    print(name.upper())
print("\n TASK 21")
# Creating a list of numbers
numbers = [10, 20, 30, 40, 50]
reversed_list = numbers[::-1]
print("Original list:", numbers)
print("Reversed list:", reversed_list)
print("\n TASK 22")
# Creating a nested list: [student_name, marks]
students = [
    ["Alice", [85, 90, 88]],
    ["Bob", [70, 75, 80]],
    ["Charlie", [95, 92, 96]],
    ["David", [60, 65, 70]]
]
for student in students:
    if student[0] == "Bob":
        print("Marks of", student[0], ":", student[1])

#Flatted Nested list
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [num for sublist in nested_list for num in sublist]
print("Flattened list:", flat_list)
print("\n TASK 23")
# Creating a list of numbers
numbers = [50, 10, 40, 20, 30]
numbers.sort()
print("Ascending order:", numbers)
numbers.sort(reverse=True)
print("Descending order:", numbers)
print("\n TASK 24")
# Creating a list of numbers
numbers = [15, 42, 7, 89, 23, 56]
max_value = max(numbers)
min_value = min(numbers)
print("Maximum value:", max_value)
print("Minimum value:", min_value)
print("\n TASK 25")
# Original list with duplicates
numbers = [10, 20, 30, 20, 40, 10, 50, 30]
unique_list = []
for num in numbers:
    if num not in unique_list:  
        unique_list.append(num)
print("Original list:", numbers)
print("List after removing duplicates:", unique_list)

















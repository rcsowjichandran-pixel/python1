# print("\n TASK 1")
# # Create a set of favorite colors
# favorite_colors = {"Red", "Blue", "Green", "Yellow", "Purple"}
# print("My favorite colors are:")
# for color in favorite_colors:
#     print(color)
# # for color in sorted(favorite_colors):
#     # print(color)
# print("\n TASK 2")
# # Create an empty set
# favorite_movies = set()
# favorite_movies.add("Inception")
# favorite_movies.add("Interstellar")
# favorite_movies.add("The Dark Knight")
# favorite_movies.add("Titanic")
# favorite_movies.add("Avengers: Endgame")
# print("My favorite movies are:", favorite_movies)
# # print("My favrite movies are:",list(favorite_movies))
# print("\n TASK 3")
# # Create a set of six fruits
# fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple"}
# fruits.remove("Mango")  
# fruits.discard("Strawberry") 
# print("Final set of fruits:", fruits)
# print("\n TASK 4")
# # Create a set of programming languages
# languages = {"Python", "Java", "C++", "JavaScript", "Ruby", "Go"}
# user_input = input("Enter a programming language: ")
# if user_input in languages:
#     print(f"{user_input} exists in the set ✅")
# else:
#     print(f"{user_input} does not exist in the set ❌")
# print("\n TASK 5")
# # Create two sets
# even_numbers = {2, 4, 6, 8, 10}
# odd_numbers = {1, 3, 5, 7, 9}
# all_numbers = even_numbers.union(odd_numbers)
# print("All numbers up to 10:", all_numbers)
# print("\n TASK 6")
# # Create two sets
# set1 = {2, 4, 6, 8, 10}
# set2 = {4, 8, 12, 16}
# common_elements = set1.intersection(set2)
# print("Common elements:", common_elements)
# print("\n TASK 7")
# # Create two sets
# setA = {1, 2, 3, 4, 5, 6}
# setB = {4, 5, 6, 7, 8, 9}
# difference = setA.difference(setB)
# print("Difference (A - B):", difference)
# print("\n TASK 8")
# # Create two sets with some common values
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# symmetric_diff = set1.symmetric_difference(set2)
# print("Symmetric Difference:", symmetric_diff)
# print("\n TASK 9")
# # Create a set of car brands
# car_brands = {"Toyota", "BMW", "Tesla", "Ford"}
# print("Car brands in the set:")
# for brand in car_brands:
#     print(brand)
# print("\n TASK 10")
# # Create a list of numbers with duplicates
# numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7, 8, 5]
# unique_numbers = set(numbers)
# print("Unique numbers:", unique_numbers)
# print("\n TASK 11")
# # Create a frozen set of vowels
# vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
# print("Frozen set of vowels:", vowels)
# try:
#     vowels.add('y')   
# except AttributeError as e:
#     print("Error:", e)
# print("\n TASK 12")
# # Create a frozen set of prime numbers up to 10
# prime_numbers = frozenset({2, 3, 5, 7})
# even_numbers = {2, 4, 6, 8, 10}
# common_elements = prime_numbers.intersection(even_numbers)
# all_elements = prime_numbers.union(even_numbers)
# print("Frozen set of primes:", prime_numbers)
# print("Set of even numbers:", even_numbers)
# print("Intersection:", common_elements)
# print("Union:", all_elements)
# print("\n TASK 13")
# # Create a set of 10 random words
# words = {"apple", "banana", "cherry", "dog", "elephant", 
#          "flower", "grape", "house", "ice", "jungle"}
# length = len(words)
# print("The set contains", length, "items.")
# print("\n TASK 14")
# # Create a dictionary with three key-value pairs
# person = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }
# print("Name (using []):", person["name"])
# print("Age (using []):", person["age"])
# print("Name (using get()):", person.get("name"))
# print("Age (using get()):", person.get("age"))
# print("\n TASK 15")
# # Create a dictionary
# person = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }
# print("Country:", person.get("country", "Unknown"))
# print("\n TASK 16")
# # Start with an empty dictionary
# person = {}
# person["name"] = "Alice"
# print("After adding name:", person)
# person["age"] = 25
# print("After adding age:", person)
# person["city"] = "New York"
# print("After adding city:", person)
# print("\n TASK 17")
# # Create a dictionary with product details
# product = {
#     "name": "Laptop",
#     "price": 50000,
#     "stock": 10
# }
# print("Before update:", product)
# product["price"] = 45000   
# product["stock"] = 15      
# print("After update:", product)
# print("\n TASK 18")
# # Create two separate dictionaries
# dict1 = {"name": "Alice", "age": 25}
# dict2 = {"city": "New York", "country": "USA"}
# print("Dictionary 1:", dict1)
# print("Dictionary 2:", dict2)
# dict1.update(dict2)
# print("Merged dictionary:", dict1)
# print("\n TASK 19")
# # Create a dictionary with five key-value pairs
# student = {
#     "name": "Alice",
#     "age": 20,
#     "grade": "A",
#     "city": "New York",
#     "course": "Computer Science"
# }
# print("Original dictionary:", student)
# del student["city"]
# print("After removing 'city':", student)
# try:
#     del student["country"]   
# except KeyError as e:
#     print("Error:", e)
# print("\n TASK 20")
# # Create a dictionary with three key-value pairs
# product = {
#     "name": "Laptop",
#     "price": 50000,
#     "stock": 10
# }
# removed_value = product.pop("price")
# print("Removed value (price):", removed_value)
# print("Updated dictionary:", product)
print("\n TASK 21")
# Create a dictionary with at least three items
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
print("Original dictionary:", student)
removed_item = student.popitem()
print("Removed item:", removed_item)
print("Updated dictionary:", student)
print("\n TASK 22")
# Create a dictionary with three key-value pairs
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
print("Student details:")
for key, value in student.items():
    print(key, ":", value)
print("\n TASK 23")
# Create a dictionary with three key-value pairs
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
print("Keys in the dictionary:")
for key in student.keys():
    print(key)
print("\n TASK 24")
# Create a dictionary with three key-value pairs
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
print("Values in the dictionary:")
for value in student.values():
    print(value)
print("\n TASK 25")
# Create a nested dictionary with student details
students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "subjects": ["Math", "Physics", "Computer Science"]
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "subjects": ["Biology", "Chemistry", "English"]
    },
    "student3": {
        "name": "Charlie",
        "age": 19,
        "subjects": ["History", "Economics", "Political Science"]
    }
}
for student_id, details in students.items():
    print(f"\n{student_id} details:")
    for key, value in details.items():
        print(f"{key} : {value}")
print("\n TASK 26")
# Create a nested dictionary with student details
students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "subjects": ["Math", "Physics", "Computer Science"]
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "subjects": ["Biology", "Chemistry", "English"]
    },
    "student3": {
        "name": "Charlie",
        "age": 19,
        "subjects": ["History", "Economics", "Political Science"]
    }
}
print("Subjects of student2 (direct indexing):", students["student2"]["subjects"])
print("Subjects of student2 (using get()):", students.get("student2").get("subjects"))






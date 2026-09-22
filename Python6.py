# Task 1: Create and Print a String
print("\n TASK 1")
greeting = "Hello, Python!"
print(greeting)

# Task 2: Access Specific Characters in a String
print("\n TASK 2")
text = "PythonProgramming"

# First character
print("First character:", text[0])

# Last character
print("Last character:", text[-1])

# Middle character
middle_index = len(text) // 2
print("Middle character:", text[middle_index])

# Task 3: Slice a String
print("\n TASK 3")
text = "Python Developer"

# Extract "Python"
print("Word 1:", text[0:6])

# Extract "Developer"
print("Word 2:", text[7:])

# Reverse the string
print("Reversed:", text[::-1])

# Task 4: Try Modifying a String
print("\n TASK 4")
text = "Immutable"
new_text = "A" + text[1:]
print(new_text)

# # Task 5: Delete a String
# print("\n TASK 5")
# temp = "Temporary String"
# print("Before deletion:", temp)

# # Delete the variable
# del temp
# # Try printing after deletion
# print("After deletion:", temp)   # ❌ This will cause an error

# temp = "Temporary String"
# temp = ""   # now it's just an empty string
# print("Cleared string:", temp)

# Task 6: Update a String
print("\n TASK 6")
text = "Hello, World!"

# Update using slicing and concatenation
updated_text = text[0:7] + "Python!"
print(updated_text)

# Task 7: Use String Methods
print("\nTASK 7")
text = "Python is Amazing!"

# Convert to uppercase
print("Uppercase:", text.upper())

# Convert to lowercase
print("Lowercase:", text.lower())

# Convert to title case
print("Title Case:", text.title())

# Replace "Amazing" with "Powerful"
print("Replaced:", text.replace("Amazing", "Powerful"))

# Task 8: Check String Properties
print("\n TASK 8")
text = "Hello123"

# Check if contains only alphabets
print("Only alphabets?", text.isalpha())

# Check if contains only digits
print("Only digits?", text.isdigit())

# Check if contains both letters and numbers
has_alpha = any(ch.isalpha() for ch in text)
has_digit = any(ch.isdigit() for ch in text)

print("Contains both letters and numbers?", has_alpha and has_digit)

# Task 9: Concatenating and Repeating Strings

# Given strings
print("\n TASK 9")
str1 = "Python"
str2 = "Programming"

# Concatenate with a space
result = str1 + " " + str2
print("Concatenated:", result)

# Repeat "Python! " 5 times
repeat_result = "Python! " * 5
print("Repeated:", repeat_result)


# Task 10: Format a String Using f-strings
print("\n TASK 10")
# Taking user input
name = input("Enter your name: ")
age = input("Enter your age: ")

# Using f-string for formatting
print(f"Hello, my name is {name} and I am {age} years old.")

# Task 11: Find and Replace a Word in a String
print("\n TASK 11")
sentence = "I love Java!"

# Replace "Java" with "Python"
updated_sentence = sentence.replace("Java", "Python")
print(updated_sentence)


# Task 12: Count the Occurrences of a Character
print("\n TASK 12")
text = "banana"

# Count how many times 'a' appears
count_a = text.count("a")

print(f"The letter 'a' appears {count_a} times.")

# Task 13: Reverse Words in a Sentence
print("\n TASK 13")
sentence = "Python is fun"

# Split the sentence into words
words = sentence.split()

# Reverse the list of words
reversed_words = words[::-1]

# Join them back into a string
result = " ".join(reversed_words)

print(result)


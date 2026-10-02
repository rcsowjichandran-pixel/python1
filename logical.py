# text=input("Enter a string:")
# reversed_text=""
# for char in text:
#     reversed_text=char+reversed_text
# print("Reversed string:",reversed_text) 
# # using while loop
# text="Sowjanya"
# reversed_text=""
# i=len(text)-1
# while i>=0:
#     reversed_text +=text[i]
#     i-=1
# print("Reversed string:", reversed_text)

# print("\n TASK 2")
# num=int(input("Enter a number:"))
# if num%2==0:
#     print(f"{num} is Even")
# else:
#     print(f"{num} is odd")

# print("\n TASK 3")
# num1 = float(input("Enter the first number:"))
# num2 = float(input("Enter the second number:"))
# num3 = float(input("Enter the third number:"))
# if num1 >= num2 and num1 >= num3:
#     print(f"{num1} is the largest number.")
# elif num2 >= num1 and num2 >= num3:
#     print(f"{num2} is the largest number.")
# else:
#     print(f"{num3} is the largest number.")
# # shorter method
# num1 = float(input("Enter the first number:"))
# num2 = float(input("Enter the second number:"))
# num3 = float(input("Enter the third number:"))
# print("The largest number is",max(num1,num2,num3))

# print("\n TASK 4")
# num1=float(input("Enter the first number:"))
# num2=float(input("Enter the second number:"))
# num3=float(input("Enter the third number:"))
# if num1<=num2 and num1<=num3:
#     print(f"{num1} is the smallest number.")
# elif num2<=num1 and num2<=num3:
#     print(f"{num2} is the smallest number.")
# else:
#     print(f"{num3} is the smallest number.")
# # Shorter method
# num1=float(input("Enter the first number:"))
# num2=float(input("Enter the second number:"))
# num3=float(input("Enter the third number:"))
# print("The smallest number is",min(num1,num2,num3))

# print("\nTASK 5")
# numbers=[12,45,7,89,34]
# largest=numbers[0]
# for num in numbers:
#     if num>largest:
#         largest=num
# print("The largest number in the list is:",largest)
# # shorter method
# numers=[12,45,7,89,34]
# largest=sorted(numbers)[-1]
# print("The largest number in the list is:",largest)

# print("\n TASK 6")
# numbers=[12,45,7,89,34]
# smallest=numbers[0]
# for num in numbers:
#     if num<smallest:
#         smallest=num
# print("The largest number in the list is:",smallest)
# # shorter method
# numers=[12,45,7,89,34]
# smallest=sorted(numbers)[0]
# print("The largest number in the list is:",smallest)


# print("\n TASK 7")
# numbers=[12,45,90,7,56,67]
# unique_numbers=list(set(numbers))
# unique_numbers.sort()
# second_largest=unique_numbers[-2]
# print("The second largest number in the list is:",second_largest)
# # using logic 
# numbers = [12, 45, 7, 89, 34, 67]
# largest = second = float('-inf')
# for num in numbers:
#     if num > largest:
#         second = largest
#         largest = num
#     elif num > second and num != largest:
#         second = num
# print("The second largest number in the list is:", second)

# print("\n TASK 8")
# numbers=[12,45,90,7,56,67]
# unique_numbers=list(set(numbers))
# unique_numbers.sort()
# second_smallest=unique_numbers[1]
# print("The second smallest number in the list is:",second_smallest)
# # using logic 
# numbers = [12, 45, 7, 89, 34, 67]
# smallest = second = float('inf')
# for num in numbers:
#     if num < smallest:
#         second = smallest
#         smallest = num
#     elif num < second and num != smallest:
#         second = num
# print("The second smallest number in the list is:", second)

# print("\n TASK 9")
# numbers=[12,45,7,89,12,34,45,7]
# unique_numbers=list(set(numbers))
# print("List after removing duplicates(unordered):",unique_numbers)
# # original order
# unique_ordered=[]
# for num in numbers:
#     if num not in unique_ordered:
#         unique_ordered.append(num)
# print("List after removing duplicates(ordered):",unique_ordered)

# print("\n TASK 10")
# numbers=[12,45,7,89,34,45,12,7]
# duplicates=[]
# for num in numbers:
#     if numbers.count(num)>1 and num not in duplicates:
#         duplicates.append(num)
# print("Duplicate elements in the list are:",duplicates)
# # Efficient Method
# numbers = [12, 45, 7, 89, 34, 45, 12, 7, 89, 100]
# seen = set()
# duplicates = set()
# for num in numbers:
#     if num in seen:
#         duplicates.add(num)
#     else:
#         seen.add(num)
# print("Duplicate elements in the list are:", list(duplicates))

# print("\n TASK 11")

# numbers = [10, 20, 10, 30, 20, 40, 10, 30, 50]
# frequency = {}
# for num in numbers:
#     if num in frequency:
#         frequency[num] += 1   # increment count if already present
#     else:
#         frequency[num] = 1    # add new entry with count 1
# print("Frequency of each element:")
# for key, value in frequency.items():
#     print(f"{key} -> {value}")
# # Another Method
# from collections import Counter

# numbers = [10, 20, 10, 30, 20, 40, 10, 30, 50]
# frequency = Counter(numbers)

# print("Frequency of each element:", dict(frequency))


# print("\n TASK 12")
# # Program to count frequency of each character in a string
# text = "banana"
# frequency = {}
# for char in text:
#     if char in frequency:
#         frequency[char] += 1   # increment count if already present
#     else:
#         frequency[char] = 1    # add new entry with count 1
# print("Character Frequency:")
# for key, value in frequency.items():
#     print(f"'{key}' -> {value}")
# # Another Method
# from collections import Counter
# text = "banana"
# frequency = Counter(text)
# print("Character Frequency:", dict(frequency))


# print("\n TASK 13")
# # Program to check if a string is a palindrome
# text = input("Enter a string: ")
# text = text.lower()
# if text == text[::-1]:
#     print("The string is a palindrome ✅")
# else:
#     print("The string is not a palindrome ❌")

# print("\n TASK 14")
# # Program to check if a number is a palindrome
# num = int(input("Enter a number: "))
# num_str = str(num)
# if num_str == num_str[::-1]:
#     print(f"{num} is a palindrome ✅")
# else:
#     print(f"{num} is not a palindrome ❌")

# print("\n TASK 15")
# # Program to check if a number is prime
# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, int(num**0.5) + 1):  
#         if num % i == 0:
#             print(f"{num} is not a prime number ❌")
#             break
#     else:
#         print(f"{num} is a prime number ✅")
# else:
#     print(f"{num} is not a prime number ❌")

# print("\n TASK 16")
# # Program to print all prime numbers between 1 and 100
# for num in range(2, 101): 
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)

# print("\n TASK 17")
# # Program to find the factorial of a number
# num = int(input("Enter a number: "))
# factorial = 1
# if num < 0:
#     print("Factorial does not exist for negative numbers ❌")
# elif num == 0 or num == 1:
#     print(f"Factorial of {num} is 1 ✅")
# else:
#     for i in range(1, num + 1):
#         factorial *= i
#     print(f"Factorial of {num} is {factorial} ✅")

# print("\n TASK 18")
# # Program to generate Fibonacci series
# n = int(input("Enter the number of terms: "))
# a, b = 0, 1
# print("Fibonacci Series:")
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b   

# print("\n TASK 19")
# # Program to find the sum of digits of a number
# num = int(input("Enter a number: "))
# digit_sum = 0
# while num > 0:
#     digit_sum += num % 10   
#     num //= 10              
# print("Sum of digits:", digit_sum)

# print("\n TASK 20")
# num = 1234
# reversed_num = int(str(num)[::-1])
# print("Reversed Number:", reversed_num)

# print("\n TASK 21")
# # Program to count the number of digits in a number

# num = int(input("Enter a number: "))

# count = 0
# temp = abs(num)   # handle negative numbers

# while temp > 0:
#     temp //= 10   # remove last digit
#     count += 1

# print("Number of digits:", count)
# another way 
# num = int(input("Enter a number: "))
# print("Number of digits:", len(str(abs(num))))


# print("\n TASK 22")
# # Program to check if a number is an Armstrong number

# num = int(input("Enter a number: "))
# num_str = str(num)
# n = len(num_str)
# armstrong_sum = sum(int(digit) ** n for digit in num_str)
# if armstrong_sum == num:
#     print(f"{num} is an Armstrong number ✅")
# else:
#     print(f"{num} is not an Armstrong number ❌")

# print("\n TASK 23")
# # Perfect number check
# num = int(input("Enter a number: "))
# sum_divisors = sum(i for i in range(1, num) if num % i == 0)

# if sum_divisors == num:
#     print(f"{num} is a Perfect number ✅")
# else:
#     print(f"{num} is not a Perfect number ❌")
# print("\n TASK 24")
# numbers = [10, 15, 20, 25, 30]
# even_sum = sum(n for n in numbers if n % 2 == 0)
# print("Sum of even numbers:", even_sum)
# print("\n TASK 25")
# numbers = [10, 15, 20, 25, 30]
# odd_sum = sum(n for n in numbers if n % 2 != 0)
# print("Sum of odd numbers:", odd_sum)
# print("\n TASK 26")
# numbers = [10, 15, 20, 25, 30]
# evens = [n for n in numbers if n % 2 == 0]
# odds = [n for n in numbers if n % 2 != 0]

# print("Even numbers:", evens)
# print("Odd numbers:", odds)
# print("\n TASK 27")
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# common = [n for n in list1 if n in list2]
# print("Common elements:", common)
# print("\n TASK 28")
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# merged = list(set(list1 + list2))
# print("Merged list without duplicates:", merged)
# print("\n TASK 29")
# numbers = [1, 2, 3, 5, 6]
# expected_sum = sum(range(min(numbers), max(numbers)+1))
# actual_sum = sum(numbers)
# missing = expected_sum - actual_sum
# print("Missing number:", missing)
# print("\n TASK 30")
# numbers = [5, 2, 9, 1, 5, 6]
# for i in range(len(numbers)):
#     for j in range(0, len(numbers)-i-1):
#         if numbers[j] > numbers[j+1]:
#             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
# print("Sorted list:", numbers)
# print("\n TASK 31")
# sentence = "Python programming is powerful and fun"
# words = sentence.split()
# longest = max(words, key=len)
# print("Longest word:", longest)
# print("\n TASK 32")
# sentence = "Python programming is powerful and fun"
# words = sentence.split()
# shortest = min(words, key=len)
# print("Shortest word:", shortest)
# print("\n TASK 33")
# sentence = "Python programming is powerful and fun"
# words = sentence.split()
# print("Number of words:", len(words))
# print("\n TASK 34")
# text = "Python Programming"
# vowels = "aeiouAEIOU"

# vowel_count = sum(1 for ch in text if ch in vowels)
# consonant_count = sum(1 for ch in text if ch.isalpha() and ch not in vowels)

# print("Vowels:", vowel_count)
# print("Consonants:", consonant_count)
# print("\n TASK 35")
# text = "Python is powerful and fun"
# no_spaces = text.replace(" ", "")
# print("String without spaces:", no_spaces)
# print("\n TASK 36")
# sentence = "Python is fun"
# reversed_words = " ".join(word[::-1] for word in sentence.split())
# print(reversed_words)   # nohtyP si nuf
# print("\n TASK 37")
# def are_anagrams(str1, str2):
#     return sorted(str1) == sorted(str2)

# print(are_anagrams("listen", "silent"))  # True
# print("\n TASK 38")
# def first_non_repeated(s):
#     for ch in s:
#         if s.count(ch) == 1:
#             return ch
#     return None
# print(first_non_repeated("swiss"))  # w
# print("\n TASK 39")
# def first_repeated(s):
#     seen = set()
#     for ch in s:
#         if ch in seen:
#             return ch
#         seen.add(ch)
#     return None
# print(first_repeated("programming"))  # r
# print("\n TASK 40")
# s = "programming"
# duplicates = {ch for ch in s if s.count(ch) > 1}
# print(duplicates)  # {'r', 'g', 'm'}
# print("\n TASK 41")
# a, b = 5, 10
# a, b = b, a
# print(a, b)  # 10 5
# print("\n TASK 42")
# numbers = [10, 20, 30, 40]
# average = sum(numbers) / len(numbers)
# print(average)  # 25.0
# print("\n TASK 43")
# list1 = [1, 2, 3, 4]
# list2 = [2, 3, 5]
# list3 = [3, 6, 2]
# common = set(list1) & set(list2) & set(list3)
# print(common)  # {2, 3}
# print("\n TASK 44")
# keys = ["name", "age", "city"]
# values = ["Alice", 25, "Chennai"]
# dictionary = dict(zip(keys, values))
# print(dictionary)
# print("\n TASK 45")
# data = {"a": 10, "b": 25, "c": 15}
# max_key = max(data, key=data.get)
# print(max_key)  # b
# print("\n TASK 46")
# data = {"a": 10, "b": 25, "c": 15}
# sorted_dict = dict(sorted(data.items(), key=lambda x: x[1]))
# print(sorted_dict)  # {'a': 10, 'c': 15, 'b': 25}
# print("\n TASK 47")
# numbers = [1, 2, 3, 4, 5]
# squares = [x**2 for x in numbers]
# print(squares)  # [1, 4, 9, 16, 25]
# print("\n TASK 48")
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # Square each number using map()
# squared = list(map(lambda x: x**2, numbers))
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print("Squared:", squared)
# print("Evens:", evens)
print("\n TASK 49")
def sum_numbers(*args):
    return sum(args)
print(sum_numbers(10, 20, 30))   # 60
print(sum_numbers(5, 15))        # 20
print("\n TASK 50")
def print_student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_student_details(name="Alice", age=20, grade="A")
# # Output:
# # name: Alice
# # age: 20
# # grade: A



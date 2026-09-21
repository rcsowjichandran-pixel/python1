print("TASK 1")
word = "PYTHON"
for char in word:
    print(char)

print("\nTASK 2")
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)


print("\nTASK 3")
text = input("Enter a string: ")
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print("Reversed string:", reversed_text)

print("\nTASK 4")
for i in range(1, 21):
    print(i)

print("\nTASK 5")
for i in range(2, 51, 2):
    print(i)

print("\nTASK 6")
for i in range(10, 0, -1):
    print(i)

print("\nTASK 7")
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    print("You entered:", num)

print("\nTASK 8")
for i in range(1, 51):
    if i % 5 == 0:
        continue
    print(i)

print("\nTASK 9")
for i in range(1, 11):
    if i == 5:
        pass  # Do nothing
    else:
        print(i)

print("\nTASK 10")
for i in range(1, 11):
    print(i)
else:
    print("Loop finished successfully")

print("\nTASK 11")
word = "HELLO"
for index, char in enumerate(word):
    print(f"Index {index}: {char}")

print("\nTASK 12")
sentence = input("Enter a sentence: ")
words = sentence.split()

for index, word in enumerate(words, start=1):
    print(f"Word {index}: {word}")

print("\nTASK 13")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print("-" * 20)  # Separator line

# print("\nTASK 14")
# while True:
#     print("Hello, World!")

# print("\nTask 15")
# import time

# start_time = time.time()

# while True:
#     print("Hello, World!")
#     if time.time() - start_time > 2:  # Stop after 5 seconds
#         break

print("\nTASK 16")
while True:
    text = input("Enter something (type 'exit' to stop): ")
    if text.lower() == "exit":
        break
    print("You entered:", text)

print("\nTASK 17")
i = 1
while i <= 20:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1

print("\nTASK 18")
while True:
    num = int(input("Enter a number: "))
    if num > 0:
        print("Positive number entered:", num)
        break
    else:
        print("Negative number ignored, try again.")

print("\nTASK 19")
i = 1
while i <= 30:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1

print("\nTASK 20")
import random

secret_number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret_number:
        print("🎉 Correct! You guessed the number.")
        break
    else:
        print("Wrong guess, try again!")

print("\nTASK 21")
correct_password = "secret123"

while True:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Access Granted ✅")
        break
    else:
        print("Wrong password, try again.")

print("\nTASK 22")
correct_pin = "1234"
attempts = 0

while attempts < 3:
    pin = input("Enter PIN: ")
    if pin == correct_pin:
        print("Access Granted ✅")
        break
    else:
        attempts += 1
        print("Incorrect PIN.")
else:
    print("Account Locked ❌")

print("\nTASK 23")
for i in range(10):
    pass  # Placeholder, does nothing

print("\nTASK 24")
for i in range(5):
    # TODO: implement later
    pass

print("\nTASK 25")
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Loop completed successfully ✅")

print("\nTASK 26")
while True:
    word = input("Enter a word: ")
    if word == "Python":
        print("You entered Python! ✅")
        break
else:
    print("You never entered 'Python'!")

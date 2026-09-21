# Mini Project 1: Word Frequency Counter

# Step 1: Take input from user
sentence = input("Enter a sentence: ")

# Step 2: Split sentence into words
words = sentence.split()

# Step 3: Create a dictionary to store word counts
frequency = {}

for word in words:
    word = word.lower()  # make case-insensitive
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Step 4: Display results neatly
print("\nWord Frequency Count:")
for index, (word, count) in enumerate(frequency.items(), start=1):
    print(f"{index}. {word} -> {count}")


print("\n MINIPRO 2")
# Mini Project 2: Triangle Pattern Generator

# Step 1: Take input from user
rows = int(input("Enter the number of rows: "))

print("Triangle Pattern:")

# Step 2: Generate triangle using nested loop
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()  # Move to next line

print("Triangle generation completed ✅")


print("\n MINIPRO 3")
# Mini Project 3: To-Do List Manager

tasks = []

while True:
    print("\n--- To-Do List Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("Type 'exit' to quit")

    choice = input("Enter your choice: ")

    if choice.lower() == "exit":
        print("Exiting To-Do List Manager... ✅")
        break

    elif choice == "1":
        task = input("Enter a task to add: ")
        tasks.append(task)
        print(f"Task '{task}' added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
            continue
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
            continue
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        try:
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Task '{removed}' removed successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    else:
        print("Invalid choice, try again.")

else:
        print("Loop finished successfully ✅")

print("\n MINIPRO 4")
# Mini Project 4: Simple Banking System

balance = 10000  # Initial balance

while True:
    print("\n--- Banking System ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("Type 'quit' to exit")

    choice = input("Enter your choice: ")

    if choice.lower() == "quit":
        print("Exiting Banking System... ✅")
        break

    elif choice == "1":
        amount = int(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid deposit amount. Try again.")
            continue
        balance += amount
        print(f"Deposited ₹{amount}. Current Balance: ₹{balance}")

    elif choice == "2":
        amount = int(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid withdrawal amount. Try again.")
            continue
        if amount > balance:
            print("Insufficient funds ❌")
            continue
        balance -= amount
        print(f"Withdrew ₹{amount}. Current Balance: ₹{balance}")

    elif choice == "3":
        print(f"Your Current Balance: ₹{balance}")

    else:
        # Using pass for future features (like transfer, loan, etc.)
        pass
        print("Invalid choice, please try again.")

else:
    print("Banking session ended successfully ✅")


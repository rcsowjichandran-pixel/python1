# Mini Project 1: Discount Calculator for a Shopping Store

# Taking total bill amount as input
print("MINI PROJECT 1: Discount Calculator")
bill = float(input("Enter your total bill amount: ₹"))

# Applying discount rules
if bill >= 5000:
    discount = bill * 0.20
elif bill >= 3000:
    discount = bill * 0.10
elif bill >= 1000:
    discount = bill * 0.05
else:
    discount = 0

# Calculating final amount
final_amount = bill - discount

# Displaying results
print(f"Discount Applied: ₹{discount:.2f}")
print(f"Final Bill Amount: ₹{final_amount:.2f}")



print("MINI PROJECT 2")
import random

# Rock, Paper, Scissors Game

# Choices
choices = ["rock", "paper", "scissors"]

# User input
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

# Computer randomly selects
computer_choice = random.choice(choices)

print(f"Computer chose: {computer_choice}")

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "scissors" and computer_choice == "paper") or \
     (user_choice == "paper" and computer_choice == "rock"):
    print("You Win!")
elif user_choice in choices:
    print("You Lose!")
else:
    print("Invalid choice. Please enter rock, paper, or scissors.")

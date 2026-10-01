print("\n MINI PRO DAY9 1")
import json
from datetime import datetime

transactions = []

def add_income(amount, description):
    transactions.append({
        "type": "income",
        "amount": amount,
        "description": description,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

def add_expense(amount, description):
    transactions.append({
        "type": "expense",
        "amount": amount,
        "description": description,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

def get_balance():
    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
    return income - expense

def save_to_file(filename="finance_data.json"):
    with open(filename, "w") as file:
        json.dump(transactions, file, indent=4)

def load_from_file(filename="finance_data.json"):
    global transactions
    try:
        with open(filename, "r") as file:
            transactions = json.load(file)
    except FileNotFoundError:
        transactions = []

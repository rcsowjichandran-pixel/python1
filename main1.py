import finance

# Load previous data
finance.load_from_file()

while True:
    print("\n--- Personal Finance Tracker ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Balance")
    print("4. Show Transactions")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amt = float(input("Enter income amount: "))
        desc = input("Enter description: ")
        finance.add_income(amt, desc)
        finance.save_to_file()

    elif choice == "2":
        amt = float(input("Enter expense amount: "))
        desc = input("Enter description: ")
        finance.add_expense(amt, desc)
        finance.save_to_file()

    elif choice == "3":
        print("Current Balance:", finance.get_balance())

    elif choice == "4":
        for t in finance.transactions:
            print(f"{t['timestamp']} - {t['type'].capitalize()} {t['amount']} ({t['description']})")

    elif choice == "5":
        print("Exiting... Data saved.")
        finance.save_to_file()
        break

    else:
        print("Invalid choice! Try again.")

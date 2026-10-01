# # Custom Exception for Out of Stock
# class OutOfStockError(Exception):
#     pass

# # Store with products and stock
# store = {
#     "Laptop": {"price": 50000, "stock": 2},
#     "Phone": {"price": 20000, "stock": 5},
#     "Headphones": {"price": 2000, "stock": 10}
# }

# cart = {}

# def add_to_cart(product, quantity):
#     try:
#         if product not in store:
#             raise KeyError("Product not available in store!")
#         if quantity > store[product]["stock"]:
#             raise OutOfStockError("Insufficient stock available!")
#         # Add to cart
#         cart[product] = cart.get(product, 0) + quantity
#         store[product]["stock"] -= quantity
#         print(f"{quantity} {product}(s) added to cart.")
#     except KeyError as e:
#         print("Error:", e)
#     except OutOfStockError as e:
#         print("Error:", e)
#     except ValueError:
#         print("Error: Invalid input!")

# def remove_from_cart(product):
#     if product in cart:
#         store[product]["stock"] += cart[product]
#         del cart[product]
#         print(f"{product} removed from cart.")
#     else:
#         print("Product not in cart!")

# def checkout():
#     if not cart:
#         print("Cart is empty!")
#         return
#     total = sum(store[p]["price"] * q for p, q in cart.items())
#     print("Total amount:", total)
#     try:
#         payment = int(input("Enter payment amount: "))
#         if payment < total:
#             raise ValueError("Invalid payment amount! Not enough money.")
#         print("Payment successful! ✅")
#         cart.clear()
#     except ValueError as e:
#         print("Error:", e)

# # --- Menu System ---
# while True:
#     print("\n--- Online Shopping Cart ---")
#     print("1. Add Item")
#     print("2. Remove Item")
#     print("3. Checkout")
#     print("4. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":
#         product = input("Enter product name: ")
#         try:
#             quantity = int(input("Enter quantity: "))
#             add_to_cart(product, quantity)
#         except ValueError:
#             print("Error: Quantity must be a number!")
#     elif choice == "2":
#         product = input("Enter product name to remove: ")
#         remove_from_cart(product)
#     elif choice == "3":
#         checkout()
#     elif choice == "4":
#         print("Exiting system... ✅")
#         break
#     else:
#         print("Invalid choice! Please try again.")


# print("\n MINI PRO 2")
# # Custom Exception for Booking Full
# class BookingFullError(Exception):
#     pass

# # Available seats (limit)
# available_seats = ["A1", "A2", "A3", "B1", "B2"]
# booked_tickets = {}

# def book_ticket(name, destination, seat):
#     try:
#         if not name.strip():
#             raise ValueError("Passenger name cannot be empty!")
#         if seat not in available_seats:
#             raise IndexError("Invalid seat selection!")
#         if seat in booked_tickets:
#             raise BookingFullError("Seat already booked!")
        
#         booked_tickets[seat] = {"name": name, "destination": destination}
#         print(f"Ticket booked successfully for {name} → {destination}, Seat: {seat}")
#     except ValueError as e:
#         print("Error:", e)
#     except IndexError as e:
#         print("Error:", e)
#     except BookingFullError as e:
#         print("Error:", e)

# def cancel_ticket(seat):
#     if seat in booked_tickets:
#         del booked_tickets[seat]
#         print(f"Ticket for seat {seat} cancelled successfully.")
#     else:
#         print("Error: No booking found for this seat!")

# def view_tickets():
#     if not booked_tickets:
#         print("No tickets booked yet.")
#     else:
#         print("\n--- Ticket Details ---")
#         for seat, details in booked_tickets.items():
#             print(f"Seat: {seat}, Name: {details['name']}, Destination: {details['destination']}")

# # --- Menu System ---
# while True:
#     print("\n--- Railway Reservation System ---")
#     print("1. Book Ticket")
#     print("2. Cancel Ticket")
#     print("3. View Tickets")
#     print("4. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":
#         name = input("Enter passenger name: ")
#         destination = input("Enter destination: ")
#         seat = input("Enter seat (e.g., A1, B2): ")
#         book_ticket(name, destination, seat)
#     elif choice == "2":
#         seat = input("Enter seat to cancel: ")
#         cancel_ticket(seat)
#     elif choice == "3":
#         view_tickets()
#     elif choice == "4":
#         print("Exiting system... ✅")
#         break
#     else:
#         print("Invalid choice! Please try again.")

# print("\n MINI PRO 3")
# import datetime

# # File to store expenses
# FILENAME = "expenses.txt"

# def add_expense(category, amount, date=None):
#     try:
#         if not category.strip():
#             raise ValueError("Category cannot be empty!")
#         if amount <= 0:
#             raise ValueError("Amount must be positive!")
#         if date is None:
#             date = datetime.datetime.now().strftime("%Y-%m-%d")
        
#         with open(FILENAME, "a") as f:
#             f.write(f"{category},{amount},{date}\n")
#         print(f"Expense added: {category} - {amount} on {date}")
#     except ValueError as e:
#         print("Error:", e)

# def view_expenses():
#     try:
#         with open(FILENAME, "r") as f:
#             expenses = f.readlines()
#         if not expenses:
#             print("No expenses recorded yet.")
#             return
#         print("\n--- All Expenses ---")
#         for exp in expenses:
#             category, amount, date = exp.strip().split(",")
#             print(f"Category: {category}, Amount: {amount}, Date: {date}")
#     except FileNotFoundError:
#         print("No expense file found. Start by adding expenses!")

# def total_expenditure():
#     try:
#         with open(FILENAME, "r") as f:
#             expenses = f.readlines()
#         total = sum(float(exp.strip().split(",")[1]) for exp in expenses)
#         print("Total Expenditure:", total)
#     except FileNotFoundError:
#         print("No expense file found. Start by adding expenses!")

# # --- Menu System ---
# while True:
#     print("\n--- Expense Tracker ---")
#     print("1. Add Expense")
#     print("2. View Expenses")
#     print("3. Total Expenditure")
#     print("4. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":
#         category = input("Enter category: ")
#         try:
#             amount = float(input("Enter amount: "))
#             add_expense(category, amount)
#         except ValueError:
#             print("Error: Amount must be a number!")
#     elif choice == "2":
#         view_expenses()
#     elif choice == "3":
#         total_expenditure()
#     elif choice == "4":
#         print("Exiting Expense Tracker... ✅")
#         break
#     else:
#         print("Invalid choice! Please try again.")

print("\n MINI PRO 4")
import csv

FILENAME = "scores.csv"

def add_score(name, subject, score):
    try:
        if not name.strip():
            raise ValueError("Student name cannot be empty!")
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100!")

        with open(FILENAME, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, subject, score])
        print(f"Score added: {name} - {subject} - {score}")
    except ValueError as e:
        print("Error:", e)

def view_scores():
    try:
        with open(FILENAME, "r") as f:
            reader = csv.reader(f)
            print("\n--- All Scores ---")
            for row in reader:
                print(f"Name: {row[0]}, Subject: {row[1]}, Score: {row[2]}")
    except FileNotFoundError:
        print("No scores file found. Start by adding scores!")

def search_score(name):
    try:
        with open(FILENAME, "r") as f:
            reader = csv.reader(f)
            found = False
            for row in reader:
                if row[0].lower() == name.lower():
                    print(f"Found: Name: {row[0]}, Subject: {row[1]}, Score: {row[2]}")
                    found = True
            if not found:
                print("No scores found for this student.")
    except FileNotFoundError:
        print("No scores file found. Start by adding scores!")

# --- Menu System ---
while True:
    print("\n--- Quiz Score Manager ---")
    print("1. Add Score")
    print("2. View All Scores")
    print("3. Search Score by Name")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        subject = input("Enter subject: ")
        try:
            score = int(input("Enter score (0–100): "))
            add_score(name, subject, score)
        except ValueError:
            print("Error: Score must be a number between 0–100!")
    elif choice == "2":
        view_scores()
    elif choice == "3":
        name = input("Enter student name to search: ")
        search_score(name)
    elif choice == "4":
        print("Exiting Quiz Score Manager... ✅")
        break
    else:
        print("Invalid choice! Please try again.")

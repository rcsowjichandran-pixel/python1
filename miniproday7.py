print("\n MINI PRO 1")
# Mini Project 1: Student Management System
students = []  
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Update Student Name")
    print("4. Show All Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        students.append(name)
        print(f"Student '{name}' added successfully!")

    elif choice == "2":
        name = input("Enter Student Name to Remove: ")
        if name in students:
            students.remove(name)
            print(f"Student '{name}' removed successfully!")
        else:
            print("Student not found!")

    elif choice == "3":
        old_name = input("Enter Student Name to Update: ")
        if old_name in students:
            new_name = input("Enter New Name: ")
            index = students.index(old_name)
            students[index] = new_name
            print(f"Student '{old_name}' updated to '{new_name}' successfully!")
        else:
            print("Student not found!")

    elif choice == "4":
        if not students:
            print("No students in the list.")
        else:
            print("Student List:", students)

    elif choice == "5":
        print("Exiting Student Management System... ✅")
        break

    else:
        print("Invalid choice, please try again.")


print("\n MINI PRO 2")
# Mini Project 2: Shopping Cart System
cart = []  # list to store products as [name, price]
while True:
    print("\n--- Shopping Cart System ---")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. View Cart")
    print("4. Checkout")

    choice = input("Enter your choice: ")

    if choice == "1":
        product_name = input("Enter Product Name: ")
        price = float(input("Enter Price: "))
        cart.append([product_name, price])
        print(f"Product '{product_name}' added successfully!")

    elif choice == "2":
        product_name = input("Enter Product Name to Remove: ")
        found = False
        for item in cart:
            if item[0] == product_name:
                cart.remove(item)
                print(f"Product '{product_name}' removed successfully!")
                found = True
                break
        if not found:
            print("Product not found in cart!")

    elif choice == "3":
        if not cart:
            print("Cart is empty.")
        else:
            total_price = sum(item[1] for item in cart)
            print("Shopping Cart:", cart)
            print("Total Items:", len(cart))
            print("Total Price:", total_price)

    elif choice == "4":
        if not cart:
            print("Cart is empty. Nothing to checkout.")
        else:
            total_price = sum(item[1] for item in cart)
            print("Final Cart:", cart)
            print("Total Items:", len(cart))
            print("Total Price:", total_price)
            print("Thank you for shopping! ✅")
        break

    else:
        print("Invalid choice, please try again.")


print("\n MINI PRO 3")
# Mini Project 3: Student Marks Analyzer using Tuples
marks = (85, 90, 78, 92, 88)
# Step 2: Calculate total, highest, lowest, and average marks
total = sum(marks)
highest = max(marks)
lowest = min(marks)
average = total / len(marks)
# Step 3: Print results
print("Marks:", marks)
print("Total Marks:", total)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
# Step 4: Convert tuple to list, modify a mark, and convert back to tuple
marks_list = list(marks)   # tuple → list
marks_list[2] = 95         # modifying 3rd subject mark
marks = tuple(marks_list)  # list → tuple

print("Updated Marks Tuple:", marks)


print("\n MINI PRO 4")
# Mini Project 4: Shopping Cart System using Tuples

# Step 1: Create a tuple with product names
cart = ("Laptop", "Phone", "Tablet", "Laptop", "Headphones")

while True:
    print("\n--- Shopping Cart System ---")
    print("1. View Cart")
    print("2. Add Product")
    print("3. Remove Product")
    print("4. Count Product Occurrences")
    print("5. Show First Three Items")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Cart:", cart)

    elif choice == "2":
        product = input("Enter Product Name to Add: ")
        cart_list = list(cart)        # convert tuple → list
        cart_list.append(product)     # add product
        cart = tuple(cart_list)       # convert back → tuple
        print(f"Product '{product}' added successfully!")

    elif choice == "3":
        product = input("Enter Product Name to Remove: ")
        cart_list = list(cart)
        if product in cart_list:
            cart_list.remove(product)
            cart = tuple(cart_list)
            print(f"Product '{product}' removed successfully!")
        else:
            print("Product not found in cart!")

    elif choice == "4":
        product = input("Enter Product Name to Count: ")
        count = cart.count(product)
        print(f"Product '{product}' appears {count} time(s) in the cart.")

    elif choice == "5":
        print("First three items:", cart[:3])  # tuple slicing

    elif choice == "6":
        print("Exiting Shopping Cart System... ✅")
        break

    else:
        print("Invalid choice, please try again.")

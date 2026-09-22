# Mini Project 1: User Profile Formatter
print("\n MINI PRO 1")
# Step 1: Take user input
full_name = input("Enter your full name: ")
age = input("Enter your age: ")
favorite_quote = input("Enter your favorite quote: ")

# Step 2: Capitalize the first letter of each word in the name
formatted_name = full_name.title()

# Step 3: Ensure age is a string (already from input, but we can be explicit)
formatted_age = str(age)

# Step 4: Convert the favorite quote to uppercase
formatted_quote = favorite_quote.upper()

# Step 5: Display the formatted output
print("\nUser Profile:")
print("-------------------------")
print(f"Name           : {formatted_name}")
print(f"Age            : {formatted_age}")
print(f"Favorite Quote : \"{formatted_quote}\"")


# Mini Project 2: Simple Password Generator
print("\n MINI PRO 2")
# Step 1: Take user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
keyword = input("Enter your secret keyword: ")

# Step 2: Use string slicing
part1 = first_name[:3]              # First 3 letters of first name
part2 = last_name[-3:]              # Last 3 letters of last name
part3 = keyword[::-1]               # Reverse the keyword

# Step 3: Concatenate and mix case
password = (part1 + part2 + part3).title()  # Title case for mix of upper/lower

# Step 4: Display the generated password
print("\nGenerated Password:")
print("-------------------------")
print(password)

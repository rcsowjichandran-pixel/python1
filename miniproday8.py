# print("\n MINI PRO 1")
# # Mini Project 1: Contact Book Application

# contacts = {}  # Empty dictionary to store contacts

# def add_contact(name, phone, email):
#     contacts[name] = {"phone": phone, "email": email}
#     print(f"Contact '{name}' added successfully!")

# def update_contact(name, phone=None, email=None):
#     if name in contacts:
#         if phone:
#             contacts[name]["phone"] = phone
#         if email:
#             contacts[name]["email"] = email
#         print(f"Contact '{name}' updated successfully!")
#     else:
#         print(f"Contact '{name}' not found!")

# def delete_contact(name):
#     if name in contacts:
#         del contacts[name]
#         print(f"Contact '{name}' deleted successfully!")
#     else:
#         print(f"Contact '{name}' not found!")

# def search_contact(name):
#     if name in contacts:
#         print(f"Found Contact: {name} -> Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
#     else:
#         print(f"Contact '{name}' not found!")

# def display_contacts():
#     if contacts:
#         print("\n--- Contact Book ---")
#         for name, details in contacts.items():
#             print(f"{name} -> Phone: {details['phone']}, Email: {details['email']}")
#     else:
#         print("No contacts available.")

# # Example Run
# add_contact("John Doe", "9876543210", "john@example.com")
# add_contact("Alice Smith", "9123456789", "alice@example.com")

# display_contacts()

# update_contact("John Doe", phone="9999999999")
# search_contact("Alice Smith")

# delete_contact("John Doe")
# display_contacts()
# print("\n MINI PRO 2")
# # Mini Project 2: Library Book Management System

# library = {}  # Empty dictionary to store books

# def add_book(book_id, title, author, copies):
#     library[book_id] = {"title": title, "author": author, "copies": copies}
#     print(f"Book '{title}' added successfully!")

# def update_book(book_id, borrowed=False, returned=False):
#     if book_id in library:
#         if borrowed:
#             if library[book_id]["copies"] > 0:
#                 library[book_id]["copies"] -= 1
#                 print(f"One copy of '{library[book_id]['title']}' borrowed.")
#             else:
#                 print(f"No copies of '{library[book_id]['title']}' available!")
#         if returned:
#             library[book_id]["copies"] += 1
#             print(f"One copy of '{library[book_id]['title']}' returned.")
#     else:
#         print(f"Book ID '{book_id}' not found!")

# def remove_book(book_id):
#     if book_id in library:
#         removed = library.pop(book_id)
#         print(f"Book '{removed['title']}' removed successfully!")
#     else:
#         print(f"Book ID '{book_id}' not found!")

# def list_books():
#     if library:
#         print("\n--- Library Collection ---")
#         for book_id, details in library.items():
#             print(f"{book_id} -> Title: {details['title']}, Author: {details['author']}, Copies: {details['copies']}")
#     else:
#         print("No books available in the library.")

# # Example Run
# add_book("Book001", "Python Programming", "Guido van Rossum", 5)
# add_book("Book002", "Data Science Essentials", "Andrew Ng", 3)

# list_books()

# update_book("Book001", borrowed=True)
# update_book("Book002", returned=True)

# remove_book("Book002")
# list_books()
print("\n MINI PRO 3")
# Mini Project 3: Student Course Enrollment System

# Step 1: Create a set of available courses
available_courses = {"Python", "Data Science", "Web Development", "AI & ML", "Cyber Security"}

# Step 2: Create an empty set for student enrolled courses
student_courses = set()

def enroll_course(course):
    if course in available_courses:
        student_courses.add(course)
        print(f"Enrolled in {course} successfully!")
    else:
        print("Course not found!")

def remove_course(course):
    if course in student_courses:
        student_courses.remove(course)
        print(f"Removed {course} from enrolled courses.")
    else:
        print(f"You are not enrolled in {course}.")

def show_enrolled_courses():
    if student_courses:
        print("\nFinal list of enrolled courses:")
        for course in student_courses:
            print("-", course)
    else:
        print("No courses enrolled yet.")

# Example Run
print("Available Courses:", available_courses)

enroll_course("Python")
enroll_course("AI & ML")
enroll_course("Blockchain")   # Not available

remove_course("Python")
remove_course("Cyber Security")  # Not enrolled

show_enrolled_courses()
print("\n MINI PRO 4")
# Mini Project 4: Unique Word Counter from a Paragraph

# Step 1: Ask the user to input a paragraph
paragraph = input("Enter a paragraph: ")

# Step 2: Convert paragraph into a set of unique words (ignore case sensitivity)
words = set(paragraph.lower().split())

# Step 3: Store common words in a frozen set
common_words = frozenset({"is", "a", "the", "and", "to", "of", "in"})

# Step 4: Remove common words from the unique words set
unique_words = words.difference(common_words)

# Step 5: Display the total unique words and print them
print("\nTotal unique words (excluding common words):", len(unique_words))
print("Unique words:")
for word in unique_words:
    print("-", word)

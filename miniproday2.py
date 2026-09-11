# Project 1Report Card Generator

# Taking student details
print("\n MINI PRO 1")
name = input("Enter student's name: ")
student_class = input("Enter student's class: ")
subject1 = int(input("Enter marks for Subject 1: "))
subject2 = int(input("Enter marks for Subject 2: "))
subject3 = int(input("Enter marks for Subject 3: "))
total = subject1 + subject2 + subject3
percentage = total / 3
print("\n===== Report Card =====")
print(f"Name       : {name}")
print(f"Class      : {student_class}")
print(f"Subject 1  : {subject1}")
print(f"Subject 2  : {subject2}")
print(f"Subject 3  : {subject3}")
print(f"Total Marks: {total}")
print(f"Percentage : {percentage:.2f}%")
print("=======================")


print("\n MINI PRO 2")
# Salary Slip Generator
name = input("Enter employee's name: ")
basic_salary = float(input("Enter basic salary: "))
allowances = float(input("Enter total allowances: "))
gross_salary = basic_salary + allowances
tax = gross_salary * 0.10
net_salary = gross_salary - tax
print("\n===== Salary Slip =====")
print(f"Employee Name : {name}")
print(f"Basic Salary  : ₹{basic_salary:.2f}")
print(f"Allowances    : ₹{allowances:.2f}")
print(f"Gross Salary  : ₹{gross_salary:.2f}")
print(f"Tax Deduction : ₹{tax:.2f}")
print(f"Net Salary    : ₹{net_salary:.2f}")
print("=======================")


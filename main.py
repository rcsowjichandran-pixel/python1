# # TASK 14
# import Python9

# print(Python9.add(10, 5))        # 15
# print(Python9.subtract(10, 5))   # 5
# print(Python9.multiply(10, 5))   # 50
# print(Python9.divide(10, 5))     # 2.0

# # TASK 19
# import Python9

# text = "Sowjanya"
# print("Reversed:", Python9.reverse_string(text))
# print("Uppercase:", Python9.to_uppercase(text))
# print("Vowel count:", Python9.count_vowels(text))

# # # task 22
# import Python9

# Python9.add_student("Sowjanya", 20, 90)
# Python9.add_student("Arun", 21, 85)
# Python9.display_students()
# Python9.remove_student("Arun")
# Python9.display_students()

# # TASK 25
import Python9
Python9.write_file("demo.txt", "Hello Sowjanya!")
print(Python9.read_file("demo.txt"))
Python9.append_file("demo.txt", "\nAppended text.")
print(Python9.read_file("demo.txt"))

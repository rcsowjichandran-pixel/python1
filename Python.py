# name = "sowji"
# age = 35
# print("Name:", name,"Age:", age)
# print("fruits","vegetables","grains")
# print("fruits","vegetables","grains", sep=", ")
# print("fruits","vegetables","grains", sep=", ", end=" ")
# print("mango","orange","apple")
# name="sowji"
# age=35
# print("My name is ",name,"and i am ",age,"years old.")
# print(f'my name is {name} and i am {age} years old.')



from abc import ABC, abstractmethod

class Shape(ABC):          # Abstract class — blueprint, can't be instantiated
    @abstractmethod
    def area(self):         # Abstract method — no implementation, just a contract
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l, self.w = l, w
    def area(self):
        return self.l * self.w

shapes = [Circle(5), Rectangle(4, 6)]
for s in shapes:
    print(s.area())

# from abc import ABC,abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         return "Woof"

# class Cat(Animal):
#     def sound(self):
#         return "Meow"

# dog = Dog()
# cat = Cat()
# print(dog.sound())
# print(cat.sound())

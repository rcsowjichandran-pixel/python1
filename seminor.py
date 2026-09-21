from abc import ABC,abstractmethod

class Animal(ABC):              # Abstract class
    @abstractmethod
    def sound(self):  
        pass

    def behaviour(self):   
        print("friendly")
        pass

class Dog(Animal):
    def sound(self):
        return "Barks"
    def behaviour(self):
        return"friendly"
    
class Cat(Animal):
    def sound(self):
        return"Meows"
    def behaviour(self):
        return "soft nature"

dog = Dog()
cat = Cat()
dog.behaviour()
print(dog.sound())  

print(dog.behaviour()) 
print(cat.sound())
# print(cat.behaviour())


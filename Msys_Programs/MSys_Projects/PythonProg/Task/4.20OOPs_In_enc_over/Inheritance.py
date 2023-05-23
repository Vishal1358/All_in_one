# Inheritance
class Animal:
    def __init__(self,name):
        self.name = name
    def move(self):
        print(f"{self.name} is moving")
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

dog = Dog("Buddy")
dog.bark()
dog.move()
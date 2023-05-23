class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def display(self):
        print(f"Name: {self._name}, Age: {self._age}")

person = Person("John", 30)
person.display()
person._age = 40 
person.display()

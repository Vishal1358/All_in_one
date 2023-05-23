class Animal:
    cool = True

    def make_sound(self,sound):
        print(f"this animal says {sound}")

class Cat(Animal):
    pass

a = Animal()
a.make_sound("Meow")
# print(a.cool)
# print(Cat.cool)
# print(Animal.cool)

print(isinstance(a, Cat))
print(isinstance(a, Animal))
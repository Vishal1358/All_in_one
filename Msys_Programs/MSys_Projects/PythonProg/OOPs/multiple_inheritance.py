class Aquatic:
    def __init__(self, name):
        # print("AQUATIC INIT")
        self.name = name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"I am {self.name} of the sea!"

class Ambulatory:
    def __init__(self,name):
        # print("AMBULATORY INIT")
        self.name = name
    
    def walk(self):
        return f"{self.name} is walking"
    
    def greet(self):
        return f"I  am {self.name} of the land"

class Penguin( Aquatic,Ambulatory):
    def __init__(self, name):
        # print("PENGUIN INIT!")
        super().__init__(name=name)

jaws = Aquatic("Vishal")
lassie = Ambulatory("Sagar")
captain_cook = Penguin("Rahul")

print(captain_cook.swim())
print(captain_cook.walk())
print(captain_cook.greet())

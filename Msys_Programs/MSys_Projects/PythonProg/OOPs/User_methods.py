class User:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} Likes {thing}"

    def is_senior(self):
        return self.age >= 25
    
    def birthday(self):
        self.age += 1 
        return f"Happy {self.age}th, {self.first}"

user1 = User("Vishal", "Hirandai", 26)  
user2 = User("Sagar", "Hirandai", 24)

# print(user1.likes("I Likes Cat's"))
# print(user2.likes("I Love it wether"))

# print(user1.initials())
# print(user2.initials())

print(user2.is_senior())
print(user1.age)
print(user1.birthday())
print(user1.age)
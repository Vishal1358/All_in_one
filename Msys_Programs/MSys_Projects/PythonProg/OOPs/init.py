class Users:
    def __init__(self,first,last):
        self.first = first
        self.last = last

user1 = Users("Vishal",'Hirandagi')
user2 = Users('Sagar','Hirandagi')
print(user1.first , user1.last)
print(user2.first, user2.last)
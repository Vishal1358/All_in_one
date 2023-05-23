users = [
    {"username": "Vishal", "tweets":["I love cake","I love cake"]},
    {"username": "Sagar", "tweets":["I love cat",]},
    {"username": "Nandu", "tweets":[]},
    {"username": "Moin", "tweets":["I love cake","I love cake"]},
    {"username": "Suhas", "tweets":["I love cake","I love cake"]},
    {"username": "Ramesh", "tweets":[]},

]

# inactive_users = list(filter(lambda u: len(u['tweets']) == 0, users))  #inactive list
# inactive_users = list(filter(lambda u: u['tweets'], users)) #active list
# print(list(inactive_users))


# only user name upper case using map and filter

# name = list(map(lambda user: user["username"].upper(), 
# filter(lambda u: not u ["tweets"], users)))
# print(name)

# here using list comprehension
user_inactive = [user["username"].upper() for user in users if not user["tweets"]]
print(user_inactive)
# num = [2,5,6,2,4,6,9]
# s=sorted(num)
# r=sorted(num, reverse=True)
# print(s)
# print(r)
# print(num)


users = [
    {"username": "vishal","tweets": ["I Love Cake","I Love Cake"]},
    {"username": "sagar","tweets":[]},
    {"username": "nandu","tweets": ["I Love Cake","I Love Cake","I Love Cake"]},
    {"username": "moin","tweets":[]},
    {"username": "rahul","tweets": ["I Love Cake"]}
]   

# this is sorted len of user
print(sorted(users,key=len))

# this is sorted username values
print(sorted(users,key=lambda user: user['username']))


print(sorted(users,key=lambda user: len(user['tweets']), reverse=True))


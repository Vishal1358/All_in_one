# dict_1 = {"a": 1,"b": 2,"c": 2,"d": 4}
# dict_1.clear()
# print(dict_1)


# dict_1 = {"a": 1,"b": 2,"c": 2,"d": 4}
# d = dict_1.copy()
# print(d)
# print(dict_1 is d)


# new_user = {}.fromkeys([])

# new_user = {}.fromkeys(["name","score","address","email"],'unknown')
# print(new_user)

# v=new_user.fromkeys(range(1,10),"unknown")
# print(v)



dict_1 = {"name":"vishal","age":26,"gender":"male","mail":"abc@gmail.com","address":"vijayapur"}
v = dict_1.get("name")
print(v)
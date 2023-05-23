def ensure(*args):
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt!"
    return "Not sure who you are..."

print(ensure("hello",75,False,"Steele"))
print(ensure(1,True,"Steele","Colt"))
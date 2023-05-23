def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("don't divide by zero please!")
    except TypeError:
        print("a and b must be ints and float")
    else:
        return (f"{a} divided by {b} is a {result}")
# print(divide(5, 2))
# print(divide(5, 2))
# print(divide(10, 'a'))
print(divide('a', 1))
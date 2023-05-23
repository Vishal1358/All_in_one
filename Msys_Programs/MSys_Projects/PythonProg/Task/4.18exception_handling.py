'''18. Write sample code for reproducing the below errors and print the 
user defined messages with the use of exception handling concept IndexError, 
TypeError, AttributeError, ValueError '''

# IndexError
try:
    a = [1,2,3,4,5]
    print(a[5])
except IndexError:
    print("Please give proper index value")

# TypeError
try:
    a = 10
    b = "Nandu"
    print(a+b)
except TypeError:
    print("Please give both side string/int")

# AttributeError
try:
    a= "Naandu"
    b = a.append(10)
    print(b)
except AttributeError:
    print("Please give correct attribute/method")

# ValueError
try:
    a = int("string")
    print(a)
except ValueError:
    print("Please give the proper data/type")
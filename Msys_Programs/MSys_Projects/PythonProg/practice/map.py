# map() function returns a map object(which is an iterator) of the results 
# after applying the given function to each item of a given iterable (list, tuple etc.)

# def addition(n):
#     return n+n

# a = (1,2,3,4,5)
# # result = list(map(addition, a))
# # print(result)
# result = list(map(lambda x:x + x, a))
# print(result)

# a = [1,2,3]
# b = [4,5,6]
# result = map(lambda x, y : x+y, a,b)
# print(list(result))

# a = ["bat","cat","rat","mat"]
# result = list(map(list, a))
# print(result)

def double_even(num):
    if num%2==0:
        return num*2
    else:
        return num*3
        
num = [1,2,3,4,5,6]
result = list(map(double_even,num))
print(result)
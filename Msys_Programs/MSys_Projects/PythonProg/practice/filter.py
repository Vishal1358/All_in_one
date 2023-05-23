# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
# function that filters vowels
# def fun(variable):
#     let = ["a","e","i","o","u"]
#     if (variable in let):
#         return True
#     return False

# variable = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# result = filter(fun, variable)

# print("The filtered letters are:")
# for s in result:
#     print(s)


# even or odd

# a = [1,2,3,4,5,6,7,8,9]

# result = filter(lambda x: x %2 != 0, a)
# print(list(result))

# result = filter(lambda x: x %2 == 0, a)
# print(list(result))



# multiplication of 3
def multi(num):
    return num%3==0

num = [1,2,4,5,6,9,7,98,3,2,6,9,99,200]

result = filter(lambda x: multi(x),num)
print(list(result))
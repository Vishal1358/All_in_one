# check even or odd number

# numbers = [1,2,3,4,5,6]
# evens = [num for num in numbers if num % 2 == 0]
# print(evens)
# odds = [num for num in numbers if num % 2 != 0]
# print(odds)

numbers = [1,2,3,4,5,6]
a = [num*2 if num % 2 == 0 else num/2 for num in numbers]
print(a)
import math

import monk

# L1 = [25,63,15,3,]
# L2 = ["“Virat”", "“Rohit”", "“Dhoni”", "“Yuvaraj”"]
# print(L1)
# print(L2)
# L1.sort()
# L2.sort()
# print(L1)
# print(L2)
# user = str(input("Write your username -: "))
# match user : 
#     case "Om" |  "Vishal"  :
#         print("You are not allowed to access the database !")
#     case "Rishabh" :
#         print("You are allowed to access the database !")
#     case _ :
#         print("You are not a company member , you are not \allowed to access the code !")

# tuple = (1,2,3,4,5,6,7,8)
# i = tuple.index(2) # index of value
# print(i) # o/p : 1
# print(tuple.index(9))

# S1 = {10,20,30,40}
# print(S1)
# S1.clear()
# print(S1)

# S1 = {10,20,30,40}
# S2 = S1.copy()
# print(S2)

# S1 = {1, 2,3,4,5}
# S2 = {1,2,3,4,5,6,7,8,9 }
# print(S1)
# print(S2)
# S3 = S2.difference(S1)
# S4 = S1.difference(S2)
# print(S3)
# print(S4)
# S1 = {10,20,30}
# S2 = {20,30,40}
# S1.difference_update(S2)
# print(S1)

# S1 = {10,20,30}
# S2 = {10,40,50}
# S3 = {40,60,10}
# S4 = S1.intersection(S2,S3)
# print(S4)

# S1 = {1,2,3,4}
# S2 = {3,4,5,6}
# S3 = {5,6,7,8}
# S4 = S1.union(S2,S3)
# print(S4)

# S1 = {1,2,3}
# S2 = {3,4,5}
# S1.update(S2)
# print(S1)

# S1 = {1,2,3,4,5}
# S2 = {2,3}
# print(S1.issuperset(S2))
# print(S1.issubset(S1))

# S1 = {1,2,3,4,5}
# S2 = {6,7,8}
# print(S1.isdisjoint(S2))

# S1 = {1,2,3,4,5}
# S2 = {2,3,6,7,8}
# S3 = S1.symmetric_difference(S2)
# print(S3)

# thisdict ={1:10, 2:20, 3:30, 4:40}
# for i, j in  thisdict.items():
# 	print(i,"->",j,end=" ")

# D1 = {1:10, 2:20, 3:30, "Name" : "Vishal", "Age" : 26}
# K = D1.keys()
# print(K)
# V = D1.values()
# print(V)
# I = D1.items()
# print(I)

# D1 = {1:10, 2:20, 3:30}
# print(D1)
# D1.clear()
# print(D1)

# L1 = [25,63,15,3,]
# L1.append([25,30,39])
# print(L1)

# L1 = [10,20,30,40]
# print(L1)
# L1.extend(25)
# print(L1)

# Creating a tuple of strings
# my_tuple = ('apple', 'banana', 'cherry', 'orange')
# new_tuple = my_tuple + ('pear', 'kiwi')
# print(new_tuple)

# tuple1 = (0, 1, 2, 3)
# tuple1[0]
# print(type(tuple1))


# def monkey_f(self):
# 	print("monkey_f() is being called")
# # replacing address of “func” with “monkey_f”
# monk.A.func = monkey_f
# obj = monk.A()

# # calling function “func” whose address got replaced
# # with function “monkey_f()”
# obj.func()

# my_dict = {'apple': 5, 'banana': 2, 'cherry': 7}
# sorted_dict = {key: value for key, value in sorted(my_dict.items())}

# print(sorted_dict)

# d = {'c': 2, 'a': 1, 'b': 3}

#     # Sort the dictionary by key
# sorted_dict = dict(sorted(d.items()))

#      # Print the sorted dictionary
# print(sorted_dict)  #output: {'a': 1, 'b': 2, 'c': 3}

# def right_rotate(lst, n):
#     return lst[-n:] + lst[:-n]

# my_list = [10, 20, 30, 40, 50, 60, 70]
# n = 3
# rotated_list = right_rotate(my_list, n)
# print(rotated_list)

# a = [1,2,3,2,4,2,4,7,8,4,5,8,6,9,2]
# d = {}
# for i in a:
#     if i % 2 == 0:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
            
# print(d)

# match = "version"
# # input="Upgraded_image_version_8.0.4.3"
# input="Upgraded"
# if match in input:
#     print("YES")
# else:
#     print("NO")

# def swap_element(lst, pos1, pos2):
#     lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
#     return lst

# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# pos1 = 3
# pos2 = 5
# swapped_lst = swap_element(lst, pos1, pos2)
# print(swapped_lst)	#output:[1, 2, 6, 4, 5, 3, 7, 8]

# Match = 'version'
# input="-8"
# print(Match+input)

# D1 = {1:10, 2:20, 3:30}
# print(D1)
# C = D1.get(1)
# C1 = D1.get(100)
# print(C)
# print(C1)

# D1 = {1:10, 2:20, 3:30}
# print(D1)
# C = D1.pop(1)
# print(D1)
# print(C)

# D1 = {1:10, 2:20, 3:30}
# print(D1)
# D1.update({1:100})
# D1.update({7:250})
# print(D1)

# D1 = {1:10, 2:20, 3:30, 4:40}
# print(D1)
# C = D1.popitem()
# print(D1)
# print(C)

# D1 = {}
# L1 = [1,2,3,4,5,6,7]
# D1 = D1.fromkeys(L1,'Iron')
# print(D1)

# List = [1,2,44,333,6,5]
# print('Original list', List)
# l = List[3]
# print(l)
# print('Example to show mutability', List)


# tuple1 = (0, 1, 2, 3)
# print(tuple1)
# print(type(tuple1))

# def add(a,b):
#     return a*b
# print(add(25,199))

# my_list = [1, 2, 3]
# my_list.extend([4, 5, 6, 8, 9, 10])
# my_list.extend([4, 5, 6])
# print(my_list)

# print(math.sqrt(-25))

# my_list = [10, 20, 30, 40, 50, 60, 70]
# print(my_list[-3]+my_list[:-3])

# match,input = 'version','Upgraded_image_version_8.0.4.3'
# if match in input:
#     print('YES')
# else:
#     print('NO')

# print(3%7)

# Match = 'version'
# input=8
# print(Match + str(input))

# Match = 'version'
# input= '8'
# print(Match+input)

# Match = 'version'
# input=8
# print(Match+input)

# def multiply(a, b):
#     if a == 0 or b == 0:           # if either a or b is zero the result should returns zero.
#         return 0
#     result = 0                          #Else result variable is use to store the result of first addition.
#     for i in range(abs(b)):     # this loop to repeatedly add abs(a) to result abs(b) times. 
#         result += abs(a)		#Absulute function will make “-ve” value in ti “+ve”.
#     if (a < 0 and b > 0) or (a > 0 and b < 0):  # It checks the signs of a and b to determine 
#         return -result     				#the sign of the result				   else:				                        # and returns the appropriate value.        
#     else:
#         return result  
    
# print(multiply(25,25))

# def multiply(a, b):
#     pr = 0
#     sig = 1
#     if a == 0 or b == 0:           # if either a or b is zero the result should returns zero.
#         return 0
    
#     while a > 0:
#         if a % 2 == 1:
#            pr += b
#         a >>=1
#         b <<=1
#     return pr 

# a = int(input())
# b = int(input())
# print(multiply(a,b))

# a = 3<<5
# print(a)

# a = float("vishal")
# print(a)

# a = 25
# b = -4
# result = 0
# for i in range(b):
#     result += a
# print(result) 

# import time
# n = 10
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()
    # start_time = time.time()
    # while time.time() - start_time < 5:   # 2 hours * 3600 seconds per hour
    #     pass

# names_list = ['Prabhu', 'Rahul', 'Arunesh', 'Sonali', 'Rakshit']
# last_char = lambda x: x[-1] # defined a lambda function to extract the last character of a string


# sorted_names = sorted(names_list, key=last_char) # Sort the names list using the last character of each word
# print(sorted_names) # Print the sorted list

# l = [1,2,5,6]
# # a = l.append(5)
# # print(l)
# b = l.extend([25])
# print(l)

# Match = 'version'
# input=8
# print(Match+input)


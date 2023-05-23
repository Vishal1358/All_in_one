# a = "silent"
# b ="listen"
# b = len(b)
# a = list(a)
# count = 0
# for i in range(len(a)):
#     if i in b:
#         count +=1
# if count == len(b):
#     print("it is a anagrams")
# else:
#     print("it is a anagrams")


# def anagrams(a,b):
#     c = sorted(a)
#     d = sorted(b)
#     count = 0
#     if len(c) == len(d):
#         for i in range(len(c)):
#             if c[i] == d[i]:
#                 # print("yes")
#                 count += 1
#         if len(c) == count:
#             return "yes it is Anagrams string"
#         else:
#             return "it is not Anagrams string"
#     else:
#         return "length of a and length b is not equal"

def anagrnms(str1,str2):
    count = 0
    for i in str1:
        if i in str2:
            count += 1
    if len(str2) == count:
        return f"{str1} and {str2} are anagrnms"            
    else :
        return f"{str1} and {str2} are not anagrnms" 
    
a = "silent"
b ="listen"
print(anagrnms(a,b))

# Write a program in which two strings are given and determine if they share a common substring. A substring may be as small as one character. The function returns either “YES” or “NO”. 

# def substring(str1,str2):
#     if str1 in str2:
#         return "YES"
#     return "NO"

# a = list("Hello")
# b = list("Hello")
# print(substring(a,b))

# a = "rturn"
# b = "hello"
# t=0
# for i in b:
#     if i in a:
#         t+=1
# if t>=1:
#     print("yes")
# else:
#     print("no")
    
    
def sub_string(str1,str2):
    for i in str1:
        if i in str2:
            return "YES"
        return "NO"    


# str1 = input("Enter the First String:")
# str2 = input("Enter the Second String:")
# print(sub_string("hello","hi")) 
print(sub_string("silent","listen")) 

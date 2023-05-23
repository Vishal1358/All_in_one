# n  = 10
# c = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         c += 1
#         print(i,end=" ")

# n = 10
# temp = n
# i = 1
# while temp > 0:
#     if n % i == 0:
#         print(i)
#     i +=1
#     temp -= 1


def factor(n,temp, i=1):
    if temp >0:
        if n % i ==0:
            return factor(n,temp - 1, i+1)
    return i
        
print(factor(15))

# n  = 5
# temp = 1
# while n > 1:
#     if n == 0:
#         print(0)
#     elif n == 1:
#         print(1)
#     else:
#         temp = temp * n
#         n -= 1 
# print(temp)

# def fact(n, temp=1):
#     if n > 1:
#         temp = temp * n
#         return fact(n - 1,temp)
#     return temp
# print(fact(10))
        
           
# print(c)
# print(l)
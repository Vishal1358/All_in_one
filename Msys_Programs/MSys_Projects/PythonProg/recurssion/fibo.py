# n = 10
# a = 0
# b = 1
# for i in range(n):
#     print(a,end=" ")
#     c = a+b
#     a = b
#     b = c

def fibonacci(n,a=0,b=1):
    if n>0:
        print(a,end=" ")
        c= a+b
        fibonacci(n-1,b,c)
    return a

fibonacci(10)
# n = 10
# a = 0
# b= 1
# i = 0
# while n > i:
#     print(a,end=" ")
#     temp = a+b
#     a = b
#     b = temp
#     i +=1

def fibo(n,a=0,b=1):
    if n > 0:
        print(a,end=" ")
        c = a+b
        a = b
        b = c
        fibo(n-1,a,b)

fibo(10)
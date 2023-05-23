def find_second_highest(A):
    n = len(A)
    for i in range(n-1,0,-1):
        for j in range(i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


arr = [4,3,2,6,8,9]
find_second_highest(arr)
print("Second Higest number in a list: ",arr[-2])

a = [1,2,45,88, 88, 88,78,980, 980, 980]
m = 0
re = 0
for i in a:
    if i > m:
        re = m
        m = i
    elif i > m and i > re:
        m = re
print(re)

# def second_highest(a,i=0,m = 0,res = 0):
#     if i > m:
#         res = m
#         m = i
#     elif i > m and i > res:
#         m = res
#     return second_highest()


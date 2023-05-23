def bubblesort(A):
    n = len(A)
    for passes in range(n-1,0,-1):
        for i in range(passes):
            if A[i] > A[i + 1]:
                A[i],A[i+1] = A[i+1], A[i]


A = [4,3,6,7,1,2]
print("Befor Sorting",A)
bubblesort(A)
print("After sorting",A)

# A = [4,3,6,7,1,2]
# n = len(A)
# for passes in range(n-1,0,-1):
#     for i in range(passes):
#         if A[i] > A[i + 1]:
#             temp = A[i]
#             A[i] = A[i + 1]
#             A[i + 1] = temp
#         print("before sort",A)
#     print("after sort",A)
def Selectionsort(A):
    n = len(A)
    for i in range(n-1):
        position = i
        for j in range(i+1, n): 
            if A[j] < A[position]:
                position = j
        temp = A[i]
        A[i] = A[position]
        A[position] = temp
    


a = [5.0,4,9,6,2,5]
# [4,5,9,6,2]
# [2,5,9,6,4]
# [2,4,9,6,5]
# [2,4,5,6,9]
print("Orginal List:", a)
# Selectionsort(a)
# print("Sorted List:", a)
n = len(a)
for i in range(n-1):
    position = i
    for j in range(i+1, n): 
        if a[j] < a[position]:
            position = j
    if position != i:
        a[i],a[position] = a[position], a[i]
    # temp = a[i]
    # a[i] = a[position]
    # a[position] = temp
    print(a)
    
print()
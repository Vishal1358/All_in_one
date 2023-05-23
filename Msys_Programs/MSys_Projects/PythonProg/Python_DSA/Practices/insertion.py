def insertion(a):
    n = len(a)
    for i in range(n-1):
        position = i
        cvalue = a[i]
        while position > 0 and a[position - 1] > cvalue:
            a[position] = a[position - 1]
            position = position - 1
        a[position] = cvalue

A = [6, 8, 2, 5, 4, 9]
print("Original array",A)
insertion(A)
print("Sorted array",A)
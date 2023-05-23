def bubble(a):
    n = len(a)
    for passes in range(n-1,-1,-1):
        for i in range(passes):
            if a[i] > a[i + 1]:
                temp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp
                


A = [6, 8, 2, 5, 4, 9]
print("Original array",A)
bubble(A)
print("Sorted array",A)
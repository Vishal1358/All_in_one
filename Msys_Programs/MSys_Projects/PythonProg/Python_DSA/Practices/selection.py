def selection(a):
    n = len(a)
    for i in range(n-1):
        position = i
        for j in range(i+1, n):
            if a[j] < a[position]:
                position = j
        temp = a[i]
        a[i] = a[position]
        a[position] = temp
a = [5,6,3,2,8,4,6]
print("Original array",a)
selection(a)
print("Sorted array",a)
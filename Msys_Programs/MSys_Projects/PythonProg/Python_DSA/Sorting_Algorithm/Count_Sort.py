def countsort(A):
    n = len(A)
    maxsize = max(A)
    carray = [0] * (maxsize + 1)
    for i in range(n):
        carray[A[i]] = carray[A[i]] + 1
    i = 0
    j = 0
    while i < maxsize + 1:
        if carray[i] > 0:
            A[j] = i
            j = j + 1
            carray[i] = carray[i] - 1
        else:
            i = i+1

A = [5,9,9,6,3,2,7,5,4,8]
print("Original List:",A)
countsort(A)
print("Sorted List:",A)

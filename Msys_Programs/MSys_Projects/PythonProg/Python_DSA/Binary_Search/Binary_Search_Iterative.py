def binarysearchiterative(A, key):
    l = 0
    r = len(A)-1

    while l<= r:
        m = (l + r)//2
        if key == A[m]:
            return m
        elif key < A[m]:
            r = m - 1
        elif key > A[m]:
            l = l + 1

    return -1

A = [25,36,38,44,56,66,68,70]
f = binarysearchiterative(A, 68)
print("result", f)
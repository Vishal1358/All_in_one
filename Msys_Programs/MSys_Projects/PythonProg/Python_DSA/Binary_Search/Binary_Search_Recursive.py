def binarysearch_recursive(A,key,l,r):
    if l > r:
        return -1
    else:
        mid = (l + r) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return binarysearch_recursive(A, key, l, mid-1)
        elif key > A[mid]:
            return binarysearch_recursive(A, key, mid+1, r)


A = [25,36,38,44,56,66,68,70]
# f = binarysearch_recursive(A, 55, 0, 7)
f = binarysearch_recursive(A, 68, 0, 7)
print("result", f)
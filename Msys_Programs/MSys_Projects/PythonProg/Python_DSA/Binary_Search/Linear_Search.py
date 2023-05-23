def linearsearch(A, key):
    index = 0
    while index < len(A):
        if A[index] == key:
            return index
        index += 1
    return -1

A = [65,25,36,35,22,99,202]
# b = linearsearch(A, 35)
b = linearsearch(A, 100)
print("result:", b)
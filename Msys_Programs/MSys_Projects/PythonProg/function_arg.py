def sum(*args):
    total = 0
    for val in args:
        total += val

    return total

print(sum(1,2,3,4))
print(sum(1,2,3,4,5,7,6,5,5,2,2,2,2,2,2,2,2,2))
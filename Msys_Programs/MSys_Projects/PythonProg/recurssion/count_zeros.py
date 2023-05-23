def count_zeros(n):
    if n>0: 
        if n % 10 == 0:
            return 1 + count_zeros(n//10)
    return 0

print(count_zeros(100000))
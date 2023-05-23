a = [num for num in range(1, 1001) if any(num % i == 0 for i in range(2, 10))]
print(a)
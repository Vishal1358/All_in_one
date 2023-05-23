numbers = list(range(1, 11))
result = []

for num in numbers:
    if num % 2 == 0:
        result.append(num ** 2)   # square of even number
    else:
        result.append(num ** 3)   # cube of odd number

print(result)

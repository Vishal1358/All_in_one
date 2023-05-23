'''5.From given list of numbers, create a list of square of prime numbers . 
l1 = [1, 4, 6, 11,15, 24, 19, 25, 27, 30,17] '''

# def is_prime(n):

#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# l1 = [1, 4, 6, 11, 15, 24, 19, 25, 27, 30, 17]

# squares_of_primes = []

# for num in l1:
#     if is_prime(num):
#         squares_of_primes.append(num ** 2)

# print(squares_of_primes)


l1 = [1, 4, 6, 11, 15, 24, 19, 25, 27, 30, 17]
l = []
for i in l1:
    if i > 1:
        for j in range(2,i):
            if i%j == 0:
                break
        if i % j != 0:
            l.append(i**2)
print(l)





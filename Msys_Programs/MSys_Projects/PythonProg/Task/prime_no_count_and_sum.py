def number_of_prime_numbers(num1, num2):
    primes = []
    for i in range(num1, num2+1):
        if i > 1:
            for j in range(2,i//2+1):
                if i % j == 0:
                    break
            else:
                primes.append(i)
    #print(primes)
    return primes,len(primes), sum(primes)

primes, count, prime_sum = number_of_prime_numbers(10, 50)
print("primes between parameters:", primes)
print("Number of primes:", count)
print("Sum of primes:", prime_sum)
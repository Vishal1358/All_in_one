def fib_gen(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x, y = y, x  + y
        yield x
        count += 1

for n in fib_gen(10):print(n)
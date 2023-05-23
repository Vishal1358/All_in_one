n = int(input('enter a number: '))
for i in range(n+1):
    for j in range(n-i):
        print(' ',end='')
    print('*', end='')
    print('-' * (2*i -1), end='')
    if i:
        print('*', end='')
    print()
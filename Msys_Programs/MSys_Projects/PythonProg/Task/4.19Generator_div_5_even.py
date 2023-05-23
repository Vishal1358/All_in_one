'''Define a generator to print the numbers between o to n (including) which are divisible by 5 and should be even 
N = 20 
Output: 10 20 '''

def generator_even(num):
    for i in range(1,num+1):
        if i % 5 == 0:
            if i % 2 == 0:
                yield i

a = generator_even(20)
for i in a:
    print(i,end=" ")
# Custom for loop

# for num in [1,2,3]
# for char in "hi there"

def my_myfor(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            # print(next(iterator))
            thing = next(iterator)
        except StopIteration:
            # print("END OF ITERATIONS")
            break
        else:
            func(thing)
        
def square(x):
    print(x*x)


# my_myfor("hello")
# my_myfor([1,2,3,4,5,6])
my_myfor("lol", print)
my_myfor([1,2,3,4,5,6],square)
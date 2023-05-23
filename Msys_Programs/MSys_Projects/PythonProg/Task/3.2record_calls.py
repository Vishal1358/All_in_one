def record_calls(func):
    def wrapper():
        wrapper.call_count += 1
        func()
    wrapper.call_count = 0
    return wrapper

@record_calls
def my_func():
    print("Hello, world!")

my_func()  
my_func()  
my_func() 
print(my_func.call_count)
def zero_division_decorator(func):
    def wrapper(num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return func(num1, num2)
    return wrapper

@zero_division_decorator
def divide(num1, num2):
    return num1 / num2

result = divide(10, 2)
print(result)  

result = divide(10, 0)
print(result)
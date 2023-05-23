try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))

    if num1 == 0 or num2 == 0:
        raise ZeroDivisionError("Divisor cannot be zero")
    
    if num1 > num2:
        result = num1 / num2
    else:
        result = num2 / num1

    print(result)
except ValueError:
    print("Input should be in iteger only!")

except ZeroDivisionError:
    print(f"Error: {ZeroDivisionError}")
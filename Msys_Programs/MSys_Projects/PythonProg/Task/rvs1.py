# function to reverse a number
def reverse_num(num):
    # initialize variables for reversed number and digit multiplier
    reverse_num = 0
    multiplier = 1
    
    # loop until all digits have been processed
    while num > 0:
        # extract the last digit of the number
        last_digit = num % 10
        
        # if the last digit is 0, multiply the multiplier by 10
        if last_digit == 0:
            multiplier *= 10
        
        # add the last digit to the reversed number
        reverse_num = (reverse_num * 10) + last_digit
        
        # remove the last digit from the number
        num //= 10
    
    # multiply the reversed number by the final multiplier (if any)
    reverse_num *= multiplier
    
    # return the reversed number
    return reverse_num

# example usage
num = 120
print("Original number:", num)
reversed_num = reverse_num(num)
print("Reversed number:", reversed_num)

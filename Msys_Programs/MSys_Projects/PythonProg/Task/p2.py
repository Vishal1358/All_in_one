def largest_num_after_removal(input_num, digit_to_remove):
    input_str = str(input_num)
    for i in range(len(input_str)):
        if int(input_str[i]) == digit_to_remove:
            return int(input_str[:i] + input_str[i+1:])
    return int(input_str)

input_num = 413234
digit_to_remove =4 
largest_num = largest_num_after_removal(input_num, digit_to_remove)
print(largest_num)  # Output: 231

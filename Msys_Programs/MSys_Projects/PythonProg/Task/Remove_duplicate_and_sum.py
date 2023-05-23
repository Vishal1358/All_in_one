# def highest_sum(input_string):
#     nums = [int(c) for c in input_string] # Convert input string to a list of integers
#     current_sum = 0
#     highest_sum = 0
#     seen = set() # Initialize a set to store seen digits
#     for num in nums:
#         if num not in seen: # If the digit has not been seen before, add it to the current sum
#             current_sum += num
#             seen.add(num)
#         else: # If the digit has been seen before, update the current sum and reset the set of seen digits
#             if current_sum > highest_sum:
#                 highest_sum = current_sum
#             current_sum = num
#             seen = {num}
#     if current_sum > highest_sum: # Check if the current sum is greater than the highest sum
#         highest_sum = current_sum
#     return highest_sum # Return the highest sum

# # Example usage
# input_string = '1211'
# print(highest_sum(input_string)) # Output: 3

# def remove_duplicates(s):
#     unique_chars = set()    # create a set to store unique characters
#     new_s = ""     # create an empty string to store characters without duplicates 
#     for char in s:      # iterate through each character in the string
#         if char not in unique_chars:   # check if the character is not already in the set 
#             unique_chars.add(char)      # add the character to the set and the new string
#             new_s += char
#     return new_s

# def highest_sum(s):
#     max_sum = 0     # initialize the maximum sum to 0
#     for i in range(len(s)):     # loop through the string s
#         new_s = remove_duplicates(s[i:])    # remove duplicates from the substring s[i:]
#         new_sum = sum(int(d) for d in new_s)    # calculate the sum of the digits in the new string
#         if new_sum > max_sum:   # update the maximum sum if the new sum is greater
#             max_sum = new_sum
#     return max_sum
# print(highest_sum('12113411')) 


# def highest_sum(input_string):
#     # Convert the input string to a list of integers
#     try:
#         digits = [int(digit) for digit in input_string]
#     except ValueError:
#         # If the input contains non-digits, return 0
#         print("Invalid input: input must only contain digits")
#         return 0
    
#     # Initialize variables
#     current_sum = 0
#     highest_sum = 0
#     seen = set()
    
#     # Loop through each digit in the input
#     for digit in digits:
#         if digit not in seen:
#             # If the digit hasn't been seen before, add it to the current sum
#             current_sum += digit
#             seen.add(digit)
#         else:
#             # If the digit has been seen before, update the highest sum and reset current sum
#             highest_sum = max(highest_sum, current_sum)
#             current_sum = digit
#             seen = {digit}
    
#     # Return the highest possible sum
#     return max(highest_sum, current_sum)

# print(highest_sum("11234sadfsdf"))

input = "121134112354465146543432165"
output = ""
c = 0
for i in input:
    if i not in output:
        output += i
        c += int(i)
print(output)
print(c)

# Initialize the input string.
# input_str = "12113421"


# output = ''.join(set(input_str))
# c = sum(int(i) for i in output)
# print(output)
# print(c)




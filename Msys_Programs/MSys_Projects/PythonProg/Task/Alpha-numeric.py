res = ""
string = input("Enter the string : ")
n = len(string)
i = 0

while i < n:
    char = string[i]

    if char.isdigit():
        res += char
        i += 1
    else:
        j = i+1
        count = 1
        while j < n and char == string[j]:
            count += 1
            j += 1
        res += char
        res += str(count)
        i = j

print(res)


# def count_alphabets(string):
#     count = 1
#     output = ""
#     for i in range(len(string)):
#         if i == 0:
#             output += string[i]
#             continue
#         if string[i].isalpha() and string[i-1].isalpha():
#             count += 1
#         else:
#             output += str(count)
#             count = 1
#         output += string[i]
#     output += str(count)
#     return output

# # Example usage
# input_string = "abb24ccc8ddbbca1"
# output_string = count_alphabets(input_string)
# print("Input string:", input_string)
# print("Output string:", output_string)        #Output string: a1b1b224c1c2c38d1d2b3b4c4a21


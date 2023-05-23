# a = [1,1,2,2,3,3,4,5]

# unique_char = []
# d = []
# prev_char = None
# for num in a:
#     if num == prev_char:
#         d.append(num)
#     else:
#         unique_char.append(num)
#         prev_char = num
# print(unique_char)



def uniques(a):
    unique_char = []
    prev_char = None
    for num in a:
        if num != prev_char:
            unique_char.append(num)
            prev_char = num
    return unique_char

a = [1,1,2,2,3,3,4,5]
print(uniques(a))
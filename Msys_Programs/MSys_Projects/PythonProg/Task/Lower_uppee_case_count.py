# my_string = "MsYs TecHNOlogiEs iS a gREat place To woRk"

# low = 0
# upper = 0
# for i in my_string:
#     if i.isalpha():
#         if i.isupper():
#             upper += 1
#         elif i.islower():
#             low +=1

# print("Lower case:",low)
# print("Upper case:",upper)

my_string = 'MsYs TecHNOlogiEs iS a gREat place To woRk#@'

uppercase_count = 0
lowercase_count = 0
for char in my_string:
    if char.isalpha():
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

print('Uppercase count:', uppercase_count)		#output: Uppercase count: 12
print('Lowercase count:', lowercase_count)			

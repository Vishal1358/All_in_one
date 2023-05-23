# a = [[1,2,3], [4,5,6], [7,8,9]]
# nested= a[-1]
# print(nested)

# a = [[1,2,3], [4,5,6], [7,8,9]]
# nested= a[-1][1]
# print(nested)
# nested= a[2][-2]
# print(nested)

a = [[1,2,3], [4,5,6], [7,8,9]]
for num in a:
    for a in num:
        print(a)
# lst1 = [1,2,1,5,9,10,2,2,7,5,3,10,8,9,15,17,21,16,17,90]
# a = len(lst1)
# b = set(lst1)
# d = len(b)
# c = a-len(b)
# print("Length of element",a)
# print("unique element",b)
# print("Length of unique element", d)
# print("Diffrence between unique and length of list",c)

lst = [1,2,1,5,9,10,2,2,7,5,3,10,8,9,15,17,21,16,17,90]

unique_count = len(set(lst))
length = len(lst)
difference = length - unique_count

print(difference)

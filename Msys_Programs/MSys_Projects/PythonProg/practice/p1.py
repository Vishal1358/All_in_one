# st = "hello"
# st1 = ""
# for i in st:
#     st1 += chr(ord(i)+3)
# print(st1)

l = ['1','2','3','4']
s = str(l)
l = list(s)
l[0],l[-1]='"','"'
print("".join(l))


# print(s[0])
# s = s.replace("[",'"')
# s = s.replace("]",'"')
# print(s)
# nums = [2,4,6,8,10]

# double = map(lambda x: x*2 ,nums)
# # list(double)
# # print(list(double))


people = ["Vishal","Sagar","Nandu","Ramesh"]
peeps = map(lambda name:name.upper(), people)
print(list(peeps))
# ['VISHAL', 'SAGAR', 'NANDU', 'RAMESH']
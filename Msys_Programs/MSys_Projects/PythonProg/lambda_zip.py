# zip 2 variable 
num1 = [1,2,3,4,5]
num2 = [6,7,8,9,10]
z=zip(num1,num2)
print(z)
print(dict(z))
l=zip(num1,num2)
print(list(l))
t=zip(num1,num2)
print(tuple(t))

# unzip all zip items
l = [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
print(list(zip(*l)))
# a = [[21,23],[45,8],[10,90]]
# a.sort(key=lambda x: x[1])
# print(a)

l = [[21,23,787,98],[45,8,65,77],[10,90,45,65]]

sort = lambda x: (sorted(x) for i in x)
secondLargest = lambda x,f: [y[len(y)-2]for y in f(x)]
res = secondLargest(l,sort)
print(res)
from functools import reduce

L1 = ["a", "b"]
L2 = [1, 2]

data = dict(zip(L1, L2))
print(data)

sum_of_values = reduce(lambda x, y: x + y, data.values())
print(sum_of_values)
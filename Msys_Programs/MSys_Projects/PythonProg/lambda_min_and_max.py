# num = [25,52,63,85,10,2,69,99]
# print(min(num))
# print(max(num))

names = ["vishal","manoj","rahul","virat","om","shivarajkumar"]
# print(min(names))
# print(max(names))

# print(max(len(names) for name in names))
# print(len(names) for name in names)
# v = [len(name) for name in names]
# print(v)

print(max(names, key=lambda n:len(n)))
print(min(names, key=lambda n:len(n)))
a = ["mom","dad", "moin","nitin","strong"]
l = []
for i in a:
    if i == i[::-1]:
        l.append(i)
print(l)

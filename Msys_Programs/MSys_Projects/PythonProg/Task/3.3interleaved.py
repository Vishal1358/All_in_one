def interleaved(l1,t2):
    l = []
    count = 0
    if len(l1) == len(t2):
        for item1, item2 in zip(l1,t2):
            count += 1
            l.append(item1)
            l.append(item2)
    else:
        return "the length of the l1 and t2 are not same"
    return l

a = [1,2,3,4,5]
b = ("a","b","c","d","e")
print(interleaved(a,b))
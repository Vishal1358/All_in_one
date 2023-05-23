
# a = [1,2,45,88, 88, 88,78,980, 980, 980]
# c = 0
# for i in a:
#     c += i
# print(c)


def lst_add(a,i=0,c=0):
    if i < len(a):
        return lst_add(a,i+1,c+a[i])
    return c

a = [1,2,45,88, 88, 88,78,980, 980, 980]
print(lst_add(a,0,0))
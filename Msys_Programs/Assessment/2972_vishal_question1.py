'''
l1 = ["siya","priya","jiya"]
l2 = [170,120,130]
'''

l1=["siya","priya","jiya"]
l2=[170,120,130]
# di={}
# final = []
# for i in range(len(l1)):
#     di[l2[i]]=l1[i]
# print(di)
# l2.sort(reverse=True)
# print(l2)
# for j in l2:
#     print(di[j])
#     final.append(di[j])
# print(final)

for i in range(len(l1)-1,0,-1):
    for j in range(i):
        if l2[j]>l2[j+1]:
            l2[j],l2[j+1]=l2[j+1],l2[j]
            l1[j],l1[j+1]=l1[j+1],l1[j]
print(l1)
print(l2)
l = [-1,-2,5,6,7,4,3,8,9,1,-1,0,100,-30]
maxv = l[0]
minv = l[0]
for i in l:
    if i > maxv:
        maxv = i
    elif i < minv:
        minv = i
print(maxv,minv)



# fs = 0
# ls = len(l)-1
# while fs <= ls:
#     if l[fs] < l[ls]:
#         l[fs], l[ls] = l[ls], l[fs]
#         fs += 1
#     else:
#         l[ls], l[fs] = l[ls], l[fs]
#         ls -= 1
# print(l)
# for i in range(0,len(l)-1):
#     if l[i] < l[i+1]:
#         l[i], l[i+1] = l[i+1], l[i]
#         # i += 1
#     else:
#         l[i],l[i+1] = l[i],l[i+1]
#         # i += 1

#     print(l)


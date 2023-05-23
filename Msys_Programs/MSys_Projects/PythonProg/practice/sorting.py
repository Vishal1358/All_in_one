# a = [5,4,7,3,2,8]
# l = len(a)-1
# for passes in range(l,0,-1):
#     for j in range(passes):
#         if a[j]>a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
    
# print(a)


s="ab"
print(s[::-1])
print("ab"[::-1])

st = "abcdefghij"
st1 = ""
k = 2
for i in range(0,len(st),k*2):
    st1 += st[i:i+k][::-1]+st[i+k:i+k*2]
print(st1)
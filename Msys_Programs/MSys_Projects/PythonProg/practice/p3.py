# l = [1,2,3,4,5,6,7,8,9,10]
# k = 2
# for i in range(0,len(l)-1,k*2):
#     l[i],l[i+1] = l[i+1], l[i]
# print(l)


# n = 15
# c = 0
# for i in range(n+1):
#     c += str(i).count("1")
# print(c)

# a = "ABCDCDC"
# a = "abababa"
# c = "ab"
a = "MBCMBCMB"
c = "MBC"
d = 0
i = 0
while i < (len(a)-1):
    str1 = a[i:i+len(c)]
    if str1 == c:
        d +=1
        i += 1
    else:
        i+=1
print(d)
    



# print(a.count(c))
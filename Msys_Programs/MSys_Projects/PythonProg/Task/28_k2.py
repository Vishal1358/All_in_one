# a = "abcdef"
# a = list(a)
# n = len(a)
# k = 2
# for i in range(0,n,2*k):
#     start = i
#     end = min(i+k-1, n-1)
#     while start<end:
#         a[start], a[end] = a[end], a[start]
#         start += 1
#         end -= 1
# print("".join(a))

def swapk2(str1,k):
    str1 = list(str1)
    n = len(str1)
    for i in range(0,n,2*k):
        start = i
        end = min(i+k-1, n-1)
        while start<end:
            str1[start], str1[end] = str1[end], str1[start]
            start += 1
            end -= 1
    return "".join(str1)

str1 = "abcdefghijk"
print(swapk2(str1,3))
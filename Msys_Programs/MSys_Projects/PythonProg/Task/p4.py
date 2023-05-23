# a = [1,2,3,4,5]
# b = a[2:]+a[:2]
# print(b)

# a = [1,2,3,4,5,3,2,1]
# lst = []
# for i in range(len(a)-1,-1,-1):
#     a[i+1]== a[i]
# print(a)

# i = []
# n = len(a)
# while n < 0:
#     i += [a[]]
#     n -= 1
# print(i)

# a = [1,2,3,4,5]
# l = len(a)-1
# while l > -1:
#     print(a[l],end=" ")
#     l -= 1

# a = [1,2,3,4,5]
# n = len(a)-1
# i = 0
# while n > i:
#     a[i],a[n] = a[n],a[i]
#     n -= 1
#     i += 1
# print(a)

st = "abc$de*%^fg"
b = "!@#$%^&*()_+=-`~[]{};':,./<>?"
lst = list(st)
f = 0
l = len(st)-1
while f<l:
    if lst[f] in b:
        f += 1
    elif lst[l] in b:
        l -= 1
    else:
        lst[l],lst[f] = lst[f],lst[l]
        f += 1
        l -= 1
print("".join(lst))

# a = 11
# for i in range(2,a):
#     if a % i == 0:
#         print("it is not prime")
#         break
# else:
    
#     print("it is prime")

# a = [1,2,3,4,5]
# n = 2
# b = a[2:]+a[:2]
# print(b)



# def binary_search(a,target):
#     start = 0
#     end = len(a)-1
#     while start <= end:
#         mid = ((start + end) //2)
#         if a[mid] == target:
#             return mid
#         elif target < a[mid] :
#             end = mid-1
#         elif target > a[mid]:
#             start = mid + 1

# a = [1,2,3,4,5,6,7]
# target = int(input())
# print(binary_search(a,target))

# def binary_search(a,target):
#     start = 0
#     end = len(a)-1
#     while start <= end:
#         mid = ((start + end) //2)
#         if a[mid] == target:
#             return mid
#         elif target > a[mid] :
#             end = mid-1
#         elif target < a[mid]:
#             start = mid + 1


# a = [8,7,6,5,4,3,2,1]
# target = int(input())
# print(binary_search(a,target))


a = [1,2,3,4,5,6,7,8]
print(a[::]) # [1,2,3,4,5,6,7,8]
print(a[::0]) # ValueError: slice step cannot be zero
print(a[::1]) #[1,2,3,4,5,6,7,8]
print(a[::-1]) #[8,7,6,5,4,3,2,1]
print(a[-1::-1]) # [8,7,6,5,4,3,2,1]
n = 4
# if n == 1:
#     return 1
# if n == 2:
#     return 2
fs = 1
ss = 1
for i in range(2,n+1):
    cs = fs + ss
    fs = cs
    ss = cs
print(ss)
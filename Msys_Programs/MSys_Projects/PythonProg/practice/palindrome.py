a = "maddam"
f = 0
l = len(a)-1
c = 0
while f < l:
    if a[f] == a[l]:
        c += 1
        f +=1
        l -=1
    else:
        break
if c == (len(a) // 2):
    print("it is pal")
else:
    print("it is not pal")


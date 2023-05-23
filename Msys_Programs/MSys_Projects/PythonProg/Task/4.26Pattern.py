a = int(input("Enter a number: "))
st = "*"
for i in range(1,a+1):
    if i%2 != 0:
        st += str(i)
        print(st)
    else:
        st += str(i)
        r = st[::-1]
        print(r)
    

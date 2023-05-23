s = "121134"
st = 0
end = len(s)
m = 1
while st<end:
    str1 = int(s[st]) * m
    if str1 == int(s[st]+1)*str1:
        print("it is repeted")
    else:
        print("it is not")
    st += 1

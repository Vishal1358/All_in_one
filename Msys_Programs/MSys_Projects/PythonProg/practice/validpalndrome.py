# s = "A man, a plan, a canal: Panama"
s = "0p"
# s = " ".join(c for c in s if c.isalnum() or c.isspace()).lower()
output = False
pal = "".join(c for c in s if c.isalnum()).lower()
if pal == pal[::-1]:
    output = True
else:
    output = False

print(output)

# def isPalindrome(s):
#     output = False
#     pal = "".join(c for c in s if c.isalnum()).lower()
#     if pal == pal[::-1]:
#         output = True
#     else:
#         output = False

#     return output
# s1 = "A man, a plan, a canal: Panama"
# print(isPalindrome(s1))

import random

caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small = "abcdefghijklmnopqrstuvwxyz"
num = "1234567890"
symbol = "!@#$%^&*()_+=-<,>.?/:;[]"
n = int(input("Enter a length: "))
password = ""
for i in range(n):
    password += random.choice(caps+small+num+symbol)
print(password)
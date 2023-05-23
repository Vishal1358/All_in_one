'''
num = 68
o/p = 5
6+8 = 14
1+4 = 5
'''

class Number:
    def add_digit(num):
        while num >= 10:
            n = 0
            while num > 0:
                n += num % 10
                num //= 10
            num = n -num
        return n
    
obj = Number
print(obj.add_digit(766))

print(88//10)
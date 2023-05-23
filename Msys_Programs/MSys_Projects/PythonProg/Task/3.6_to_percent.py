import re
# a = input("enter a number : ")
# x = re.split("\D",a)
# per = int(x[0])/int(x[-1])*100
# print(round(per,2),"%")

def to_percent(num):
    try:
        if ":" in num:
            x = re.split(":",num)
        else:
            x = re.split("/",num)
        num = int(x[0])/int(x[-1])
        per = num * 100
        return round(per,2)
    except:
        return "Enter a valid function"
a = input("enter a number : ")
print(to_percent(a))
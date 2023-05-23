def argument(*args):
    result = 0
    for i in args:
        result += i
    print(result)
argument(4,3,2,1,5)

def keyword_argument(**kwargs):
    result = 0
    for i in kwargs.values():
        result += i
    print(result)
keyword_argument(a=2,b=6,c=4)
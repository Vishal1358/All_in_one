class Row:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

row = Row(a=1, b=2,c=3)
print(row.a)
print(row.b)
print(row.c)

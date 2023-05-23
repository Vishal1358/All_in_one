# 1.parameters
# 2.*args
# 3.default_parameters
# 4.**kwargs

def display_info(a, b, *args, instructor="Colt",**kwargs):
    return [a, b, args, instructor, kwargs]
    # print(type(args))

print(display_info(1, 2, 3, last_name="vishal", job="Instructor"))

# a - 1
# b - 2
# args (3)
# instructor - "Colt"
# kwargs - {'last_name':"vishal", "job":"Instructor"}

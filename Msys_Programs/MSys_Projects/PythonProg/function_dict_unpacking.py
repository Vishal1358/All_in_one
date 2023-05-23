# def display_name(first,second):
#     print(f"{first} says hello to {second}")

# name = {"first": "colt", "second": "Rusty"}

# display_name(**name)


def add_and_multiply_number(a,b,c):
    print(a+b*c)

data = dict(a=1,b=2,c=3)
add_and_multiply_number(**data)
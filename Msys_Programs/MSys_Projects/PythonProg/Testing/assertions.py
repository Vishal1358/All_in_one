# def add_positive_number(x, y):
#     assert x > 0 and y > 0, "Both number must be positive"
#     return x + y

# print(add_positive_number(1, 1))
# add_positive_number(1, -1)

def eat_junk(food):
    assert food in [
        "pizza",
        "ice cream",
        "candy",
        "fried butter"
    ], "food must be a junk food!"
    return f"NOM NOM NOM I am eating {food}"

food = input("ENTER A FOOD PLEASE: ")
print(eat_junk(food))
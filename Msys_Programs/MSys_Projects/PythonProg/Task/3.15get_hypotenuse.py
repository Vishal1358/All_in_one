def get_hypotenuse(side1, side2):
    hypotenuse = (side1**2 + side2**2)**0.5
    return hypotenuse

side1 = int(input("Enter a number: "))
side2 = int(input("Enter a number: "))
print(get_hypotenuse(side1,side2))
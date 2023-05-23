def colorize(text, color):
    colors = ("red","blue","black", "yellow", "white")
    if type(text) is not str:
        raise TypeError("text must be instance of str")
    if color not in colors:
        raise ValueError("color invalid color")
    print(f"Printed {text} in {color}")

# colorize("hello", "pink")
colorize("hello", "red")
# colorize(34, "red")
# colorize([], "red")
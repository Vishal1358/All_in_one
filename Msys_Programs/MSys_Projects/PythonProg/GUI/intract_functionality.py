from ipywidgets import interact , interactive, fixed
import ipywidgets as widgets

def func(x):
    return x

# a = (interact(func, x=10))
a = interact(func,x=fixed("Hello"))
print(a)
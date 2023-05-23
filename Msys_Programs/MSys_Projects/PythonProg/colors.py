# import termcolor
from termcolor import colored
# print(dir(termcolor))

# text = colored("Hi Vishal!", color="red", on_color="on_yellow")
text = colored("Hi Vishal!", color="cyan", on_color="on_green", attrs=["blink"])
# text = colored("Hi Vishal!", color="cyan")
# text = colored("Hi Vishal!", color="cyan")
# text = colored("Hi Vishal!", color="yellow")
print(text)
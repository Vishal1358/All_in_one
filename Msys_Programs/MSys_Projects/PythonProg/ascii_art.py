from pyfiglet import figlet_format

msg = input("What would you like to print? ")
color = input("WHat color? ")

ascii_art = pyfiglet.figlet_format(msg)
print(ascii_art)
'''7 In the given string, remove the special characters and add a space instead of that  
"Msys&Technologies@Chennai*" '''


def special_char(input):
    string = ""
    for i in input:
        if i in "!@#$%^&*()_+=-":
            string += " "
        else:
            string += i

    print(string)

input = "Msys&Technologies@Chennai*"
special_char(input)
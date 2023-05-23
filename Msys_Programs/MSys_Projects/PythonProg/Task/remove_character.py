def remove_character(input_string, char):
    if char not in input_string:
        raise Exception("Given character is not present in the string.")
    else:
        return input_string.replace(char, '')
input_string = input("Enter a string: ") #Vishal Hirandagi
char = input("Enter the character to remove: ")   #and

try:
    result_string = remove_character(input_string, char)
    print(f"Result: {result_string}")
except Exception as e:
    print(e)

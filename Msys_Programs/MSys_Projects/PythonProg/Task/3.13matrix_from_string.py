def matrix_from_string(string):
    l = []
    for i in string:
        if i.isnumeric():
            l.append(float(i))
    return [l]

string = input("Enter a value: ")
print(matrix_from_string(string))
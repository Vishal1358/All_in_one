def string_count(string):
    E_str = ""
    count = 0
    while count < len(string):
        x = string[count]
        count += 1
        E_str += x
        E_str += str(count)
    print(E_str)

string = "abcde"
string_count(string)

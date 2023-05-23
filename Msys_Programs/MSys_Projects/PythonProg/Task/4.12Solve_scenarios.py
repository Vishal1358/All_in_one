def Solve_scenarios(string1,string2):
    str1 = (string1,)
    str2 = (string2,)
    str1 += str2

    return str1

string1 = input("Enter username: ")
string2 = input("Enter password: ")
print(Solve_scenarios(string1,string2))


try:
    print("msys" + 2007) 
except:
    print("Error: Cannot concatenate String and Number")
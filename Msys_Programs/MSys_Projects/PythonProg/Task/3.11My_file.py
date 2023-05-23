# def last_lines(file_path, n):
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#         return [line.rstrip() for line in reversed(lines[-n:])]

# for line in last_lines(r'D:\Msys_Programs\MSys_Projects\PythonProg\Task\my_file.txt',3):
#     print(line)
    
file = open(r"D:\Msys_Programs\MSys_Projects\PythonProg\Task\my_file.txt", "r")
new = file.readlines()
rev = new[::-1]
for i in rev:
    i = i.replace("\n" , "")
    print(i)

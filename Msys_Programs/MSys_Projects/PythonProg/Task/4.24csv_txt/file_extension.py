import os
import shutil

# os.mkdir(path="D:/Msys_Program/Msys_Programs/MSys_Projects/PythonProg/Task/4.24csv_txt/csv")
# os.mkdir(path="D:/Msys_Program/Msys_Programs/MSys_Projects/PythonProg/Task/4.24csv_txt/txt")

for i in os.listdir(path="D:/Msys_Program/Msys_Programs/MSys_Projects/PythonProg/Task/4.24csv_txt"):
    print(i)
    if ".csv" in i:
        shutil.move("D:/Msys_Program/Msys_Programs/MSys_Projects/PythonProg/Task/4.24csv_txt/file1.csv","D:/Msys_Program/Msys_Programs/MSys_Projects/PythonProg/Task/4.24csv_txt/csv")
        shutil.move("D:/Msys_Program/Msys_Programs/MSys_Projects/PythonProg/Task/4.24csv_txt/file2.csv","D:/Msys_Program/Msys_Programs/MSys_Projects/PythonProg/Task/4.24csv_txt/csv")
    elif ".txt" in i:
        shutil.move("D:/Msys_Program/Msys_Programs/MSys_Projects/PythonProg/Task/4.24csv_txt/file1.txt","D:/Msys_Program/Msys_Programs/MSys_Projects/PythonProg/Task/4.24csv_txt/txt")
        shutil.move("D:/Msys_Program/Msys_Programs/MSys_Projects/PythonProg/Task/4.24csv_txt/file2.txt","D:/Msys_Program/Msys_Programs/MSys_Projects/PythonProg/Task/4.24csv_txt/txt")


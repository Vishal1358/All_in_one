with open("File1.txt","r") as file1:
    txt = file1.readline().split()
dict1 = {}
with open("File2.txt","r") as file2:
    for i in file2:
        text_name, txt= i.split("-")
        dict1[text_name] = txt.strip()
    print(dict1)
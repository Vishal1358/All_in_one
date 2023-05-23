def file_name(*args):
    for i in args:
        with open(i, "r") as file:
            for j in file.readlines():
                if len(j.rstrip()) > 40:
                    yield j.rstrip()


var = file_name("file1.txt","file2.txt")
for i in var:
    print(i)

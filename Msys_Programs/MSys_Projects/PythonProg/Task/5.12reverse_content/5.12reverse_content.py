with open("file.txt", 'r') as file:
    content = file.readlines()
content.reverse()
with open("file.txt", 'w') as file1:
    for line in content:
        file1.write(line)

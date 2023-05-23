def sum_int_inFile(file):
    with open(file, "r") as file:
        text = file.read().splitlines()
        print(text)
    total = 0
    line_sum = ""
    for i in range(len(text)):
        for j in text[i]:
            if j in "123456789":
                line_sum += j
        total += int(line_sum)
        print(f"Sum of digit in line {i + 1} is {line_sum}")
        line_sum = ""
    print("Total sum is: ", total)


file1 = "file.txt"
sum_int_inFile(file1)

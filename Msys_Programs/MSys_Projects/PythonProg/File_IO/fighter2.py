from csv import reader
with open("fighter2.csv") as file:
    csv_reader = reader(file, delimiter="|")
    for row in csv_reader:
        print(row)
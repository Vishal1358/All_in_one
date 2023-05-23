# BAD Way to run!!

# with open("fighter.csv") as file:
#     data=file.read()

# using reader
# from csv import reader
# with open("fighter.csv") as file:
#     csv_reader = reader(file)
#     for row in csv_reader:
#         print(row)


# from csv import reader
# with open("fighter.csv") as file:
#     csv_reader = reader(file)
#     for fighter in csv_reader:
#         print(f"{fighter[0]} is from {fighter[1]} ")
#         # each row is a list!
  
# from csv import reader
# with open("fighter.csv") as file:
#     csv_reader = reader(file)
#     data = list(csv_reader)
#     print(data)

# using DictReader method
from csv import DictReader
with open("fighter.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # each row is an orderedDict!
        print(row)
        # print(row["Name"])
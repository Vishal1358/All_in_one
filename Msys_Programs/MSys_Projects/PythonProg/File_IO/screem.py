from csv import reader, writer

# with open("fighter.csv") as file:
#     csv_reader = reader(file)
#     fighters1 = [[s.upper() for s in row] for row in csv_reader]

# with open("screaming_fighter.csv","w") as file:
#     csv_reader = writer(file)
#     for fighter in fighters1:
#         csv_reader.writerow(fighter)



with open("fighter.csv") as file:
    csv_reader = reader(file)
    # fighters1 = [[s.upper() for s in row] for row in csv_reader]

    with open("screaming_fighter.csv","w") as file:
        csv_writer = writer(file)
        for fighter in csv_reader:
            csv_writer.writerow([s.upper() for s in fighter])
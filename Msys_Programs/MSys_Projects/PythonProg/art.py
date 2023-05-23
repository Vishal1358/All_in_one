# for x in range(3):
#     for num in range(1,11):
#         print("\U0001f600"* num)



# time = 1
# while time < 11:
#     print("\U0001f600"* time)
#     time += 1


#without string multiplication - ugly solution

for num in range(1,11):
    count = 1
    smileys = ""
    while count <= num:
        smileys += "\U0001f600"
        count += 1
    print(smileys)
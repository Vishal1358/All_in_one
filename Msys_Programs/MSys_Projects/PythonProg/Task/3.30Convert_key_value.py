def list_to_key_value(list):
    Dict = {}
    for i in list:
           Dict.update({int(str(i)[:len(str(i))//2]):int(str(i)[len(str(i))//2:])})
    return Dict
list = [2323, 82, 1293885, 95]
print(list_to_key_value(list))

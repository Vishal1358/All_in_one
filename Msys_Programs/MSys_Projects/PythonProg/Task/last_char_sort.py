def last_char(s):
    return s[-1]

names_list = ['Prabhu', 'Rahul', 'Arunesh, ''Sonali'', ''Rakshit']
sorted_names = sorted(names_list, key=last_char)
print(sorted_names)
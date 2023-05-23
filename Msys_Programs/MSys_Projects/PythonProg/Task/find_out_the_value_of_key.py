dictionary = {'India': 'New Delhi', 'USA': 'Washington D.C.', 'Nepal': 'Kathmandu'}  # Given dictionary


list_keys = list(dictionary.keys())                # to get the keys in separate lists
list_values = list(dictionary.values())          # to get the values in separate lists


print("The keys are:", list_keys)                 # to print the keys lists
print("The values are:", list_values)           # to print the values lists


key = input("Enter the Value: ")                # to take user value input for search. 
value = dictionary.get(key, 'NA')                # try to get the value of a key that does not exist.

print("The value of", key, "is", value)
# dictionary = {'Msys Technologies': 'Sanjay Sehgal', 'Infosys': 'Salil Parekh', 'TCS': 'Rajesh Gopinathan', 'Wipro': 'Thierry Delaporte'}		# Given dictionary


# values_list = list(dictionary.values())             # to get the values from dictionary n stored in values list
# sorted_values = sorted(values_list)                     # to sort the values in alphabetical order.


# print("The sorted list of values is:", sorted_values)



dictionary = {'Msys Technologies':'Sanjay Sehgal', 'Infosys':'Salil Parekh', 'TCS':'Rajesh Gopinathan', 'Wipro':'Thierry Delaporte'}

# Get all the values from the dictionary
values = list(dictionary.values())
values.sort()

print(values)

input_data = {
    'Department': ['Bakkt', 'Cisco'],
    'Team': ['Red', 'Yellow', 'Black']
}

output = []

for department in input_data['Department']:
    for team in input_data['Team']:
        output.append({
            'Department': department,
            'Team': team
        })
print(output)

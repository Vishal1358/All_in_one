def winner_table():
    num_of_teams = int(input("Enter number of teams: "))
    teams = {}
    result = {}
    index = 0
    for i in range(1,num_of_teams+1):
        team = eval(input(f"enter team {i} win, draws, loses eg(1,2,3)"))
        teams.update({"Team" + str(i):team})
        for j in range(len(team)):
            rest = (team[index]*3)+(team[index+1]*1)+(team[index+2]*-1)
            result.update({"Team"+str(i):rest})

    print(teams)
    # print(rest)
    Max = max(result, key = lambda x:result[x])

    print("Winner is : ",Max)

winner_table()
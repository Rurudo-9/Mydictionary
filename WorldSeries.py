Base_y = 1903


year_dict = {}
count_dict = {}

file = open("WorldSeriesWinners.txt", "r")
team_name = file.readline()

for team in team_name:
    name = team.strip()

file.close()

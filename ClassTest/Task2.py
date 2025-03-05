team_1: int = int(input("Qty 1 team: "))
team_2: int = int(input("Qty 2 team: "))

def competition(team_1, team_2):
    if team_1 == team_2:
        return team_1
    return team_1 * team_2

print(competition(team_1, team_2))
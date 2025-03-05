team_1: int = int(input("Qty 1 team: "))
team_2: int = int(input("Qty 2 team: "))

def competition(team_1, team_2):
    if team_1 == team_2:
        return team_1
    max_current = team_1 * team_2
    for i in range(min(team_1, team_2), max_current + 1):
        if i % team_1 == 0 and i % team_2 == 0:
            return i

print(competition(team_1, team_2))
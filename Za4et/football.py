class Player:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def __str__(self):
        return f"- Name: {self.name}\n- Age: {self.age}\n- Position: {self.position}"


class Team:
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []

    def add_player(self, player):
        if player not in self.players:
            self.players.append(player)
            print(f"Игрок {player.name} добавлен в команду {self.team_name}")
        else:
            print(f"Игрок {player.name} уже есть в команде {self.team_name}")

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)
            print(f"Игрок {player.name} удален из команды {self.team_name}")
        else:
            print(f"Игрока {player.name} нет в команде {self.team_name}")

    def list_players(self):
        print(f"\nСостав команды {self.team_name} (тренер: {self.coach}):")
        if not self.players:
            print("В команде пока нет игроков")
        else:
            for player in self.players:
                print(player)
                print()


if __name__ == "__main__":
    player1 = Player("Трамп", 25, "Нападающий")
    player2 = Player("Лукашенко", 30, "Полузащитник")
    player3 = Player("Путин", 28, "Защитник")

    team1 = Team("Красные", "Сталин")
    team2 = Team("Синие", "Горбачев")

    team1.add_player(player1)
    team1.add_player(player2)
    team2.add_player(player3)

    team1.list_players()
    team2.list_players()

    team1.remove_player(player2)
    team1.list_players()
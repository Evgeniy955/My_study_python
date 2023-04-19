class Add_result():
    total_goals_scored = 0
    total_goals_conceded = 0
    games_won = 0
    games_lost = 0
    games_draw = 0
    WIN_SCORE_WEIGHT = 3
    DRAW_SCORE_WEIGHT = 1

    def addGame(self, goals_scored, goals_conceded):
        self.total_goals_scored += goals_scored
        self.total_goals_conceded += goals_conceded
        if goals_scored > goals_conceded:
            self.games_won += 1
        elif goals_scored < goals_conceded:
            self.games_lost += 1
        else:
            self.games_draw += 1

    def get_score(self):
        self.score = self.games_won * self.WIN_SCORE_WEIGHT + self.games_draw * self.DRAW_SCORE_WEIGHT
        return f'Кол-во очков: {self.score}'

    def difference_goals(self):
        self.goals = abs(self.total_goals_scored - self.total_goals_conceded)
        return f'Разница голов: {self.goals}'


class Total_game(Add_result):
    def totalGame(self):
        self.game = self.games_won + self.games_lost + self.games_draw
        return f'Кол-во игр: {self.game}'


f = Total_game()
f.addGame(3, 1)
f.addGame(1, 1)
f.addGame(2, 3)
f.addGame(4, 2)
print(f.get_score())
print(f.difference_goals())
print(f.totalGame())

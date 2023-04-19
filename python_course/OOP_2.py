class Football:
    games_won = 0
    draws = 0
    games_lost = 0
    goal_score = 0
    goal_concede = 0
    score = 0

    # goals_scored = 0
    # goals_conceded = 0

    def numb_goals(self, goals_s, goals_c):
        goals_total = None
        while True:
            try:
                goals_total = (input(f"Enter the number of goals in a {goals_s},{goals_c} format: "))
            except ValueError:
                print("Please enter a number. Try again")
                continue
            return goals_total

    def club_total(self):
        goal_total = Football.numb_goals(self, '{scored}', '{conceded}')
        self.goalScore = abs(int(goal_total[0]))
        self.goalConcede = abs(int(goal_total[2]))
        result = input("Хотите добавить результат матча? Enter 'y' or press Enter button: ")
        if result == 'y':
            Football.club_total(self)


    def score_club(self):
        if self.goalScore > self.goalConcede:
            self.score += 3
        elif self.goalScore == self.goalConcede:
            self.score += 1
        print(f'Score: {self.score}')

    def goals(self):
        self.goal_score += self.goalScore
        self.goal_concede += self.goalConcede
        print(f'Goals scored: {self.goal_score}')
        print(f'Goals conceded: {self.goal_concede}')


class Total_game(Football):
    def total_game(self):
        if self.goalScore > self.goalConcede:
            Football.games_won += 1
        elif self.goalScore > self.goalConcede:
            Football.games_lost += 1
        elif self.goalScore == self.goalConcede:
            Football.draws += 1
        print(f'Games won: {Football.games_won}')
        print(f'Lost games: {Football.games_lost}')
        print(f'Draws: {Football.draws}')


if __name__ == '__main__':
    f = Total_game()
    f.club_total()
    f.score_club()
    f.goals()
    f.total_game()

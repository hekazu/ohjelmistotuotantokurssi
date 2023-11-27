class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points = self.player1_points + 1
        else:
            self.player2_points = self.player2_points + 1

    def formulate_tie_score(self):
        if self.player1_points == 0:
            return "Love-All"
        elif self.player1_points == 1:
            return "Fifteen-All"
        elif self.player1_points == 2:
            return "Thirty-All"
        else:
            return "Deuce"

    def formulate_endgame_score(self):
        point_difference = self.player1_points - self.player2_points

        if point_difference == 1:
            return "Advantage " + self.player1_name
        elif point_difference >= 2:
            return "Win for " + self.player1_name
        elif point_difference == -1:
            return "Advantage " + self.player2_name
        else:
            return "Win for " + self.player2_name

    def formulate_normal_score(self):
        points_as_string = ["Love", "Fifteen", "Thirty", "Forty"]
        return points_as_string[self.player1_points] + "-" + points_as_string[self.player2_points]

    def game_is_tied(self):
        return self.player1_points == self.player2_points

    def game_is_in_endgame(self):
        return self.player1_points >= 4 or self.player2_points >= 4

    def get_score(self):
        if self.game_is_tied():
            return self.formulate_tie_score()
        elif self.game_is_in_endgame():
            return self.formulate_endgame_score()
        else:
            return self.formulate_normal_score()

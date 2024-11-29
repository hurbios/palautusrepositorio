class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_even_score(self, points):
        scores = ["Love-All", "Fifteen-All", "Thirty-All", "Deuce"]
        return scores[points] if points < 3 else scores[3]

    def get_winning_player_score(self, points):
        player = "2" if points < 0 else "1"
        return f"Win for player{player}" if abs(points) > 1 else f"Advantage player{player}"

    def get_scores_from_points(self, points1, points2):
        scores = ["Love", "Fifteen", "Thirty", "Forty"]
        return f"{scores[points1]}-{scores[points2]}"

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.get_even_score(self.m_score1)
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            minus_result = self.m_score1 - self. m_score2
            return self.get_winning_player_score(minus_result)
        else:
            return self.get_scores_from_points(self.m_score1, self.m_score2)

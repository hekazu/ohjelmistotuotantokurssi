from player import Player
from player_reader import PlayerReader

def sort_by_points(player):
    return player.points

class PlayerStats:
    def __init__(self,player_reader):
        self.reader = player_reader

    def top_scorers_by_nationality(self, nationality):
        all_players = self.reader.get_players()

        players = [ player for player in all_players if player.nat == nationality ]
        players.sort(reverse=True, key=sort_by_points)

        return players

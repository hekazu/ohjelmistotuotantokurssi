import requests
from player import Player

class PlayerReader:
    def __init__(self,json_url):
        self.url = json_url

    def get_players(self):
        players_dict = requests.get(self.url).json()

        players = []

        for player_dict in players_dict:
            player = Player(player_dict)
            players.append(player)

        return players

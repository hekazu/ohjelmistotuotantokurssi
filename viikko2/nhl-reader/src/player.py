class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nat = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.penalties = dict['penalties']
        self.team = dict ['team']
        self.games = dict['games']
    
    def __str__(self):
        return self.name

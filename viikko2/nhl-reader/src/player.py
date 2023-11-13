class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nat = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.penalties = dict['penalties']
        self.team = dict ['team']
        self.games = dict['games']

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} {self.team}  {self.goals:2} + {self.assists:2} = {self.goals+self.assists}"
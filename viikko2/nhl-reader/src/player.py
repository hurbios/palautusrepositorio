class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.points = int(dict['goals']) + int(dict['assists'])
        self.nationality = dict['nationality']
    
    def __str__(self):
        return f"{self.name:25} {self.team:6} {self.goals:3} + {self.assists:3} = {int(self.assists) + int(self.goals)}"

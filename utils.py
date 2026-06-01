import json

class GameData:
    def __init__(self, player_name, score, level):
        self.player_name = player_name
        self.score = score
        self.level = level

    def to_dict(self):
        return {
            'player_name': self.player_name,
            'score': self.score,
            'level': self.level
        }

    @staticmethod
    def from_dict(data):
        return GameData(
            player_name=data['player_name'],
            score=data['score'],
            level=data['level']
        )

def save_game_data(file_path, game_data):
    with open(file_path, 'w') as f:
        json.dump(game_data.to_dict(), f)

def load_game_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        return GameData.from_dict(data)

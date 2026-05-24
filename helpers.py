import json
import random

class GameData:
    def __init__(self):
        self.data = []

    def add_event(self, event_type, details):
        event = {
            'id': self.generate_id(),
            'type': event_type,
            'details': details,
            'timestamp': self.current_timestamp()
        }
        self.data.append(event)

    def generate_id(self):
        return random.randint(1000, 9999)

    def current_timestamp(self):
        from datetime import datetime
        return datetime.now().isoformat()

    def to_json(self):
        return json.dumps(self.data, indent=4)

    def clear_data(self):
        self.data = []

# Example usage:
# game_data = GameData()
# game_data.add_event('move', {'x': 10, 'y': 20})
# print(game_data.to_json())
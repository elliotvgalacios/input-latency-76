import time
import json
import random

def simulate_input_event():
    chance = random.random()
    if chance < 0.05:
        raise Exception('Simulated input failure')
    return {'event': 'button_press', 'timestamp': time.time()}

class InputProcessor:
    def __init__(self):
        self.events = []

    def process_event(self):
        try:
            event = simulate_input_event()
            self.events.append(event)
            return event
        except Exception as e:
            error_message = {'error': str(e), 'timestamp': time.time()}
            self.events.append(error_message)
            return error_message

    def get_events(self):
        return json.dumps(self.events)

if __name__ == '__main__':
    processor = InputProcessor()
    for _ in range(10):
        processor.process_event()
    print(processor.get_events())
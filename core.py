import time
import random

class Game:
    def __init__(self):
        self.input_latency = 0.1
        self.start_time = None

    def start_game(self):
        self.start_time = time.time()
        print('Game started!')

    def simulate_input(self, user_input):
        if self.start_time is None:
            raise ValueError('Game has not started.')
        if user_input not in ['jump', 'duck', 'run']:
            raise ValueError('Invalid input. Valid inputs are: jump, duck, run.')
        latency = random.uniform(0, self.input_latency)
        time.sleep(latency)
        print(f'Input received: {user_input} after {latency:.3f} seconds')

    def get_elapsed_time(self):
        if self.start_time is None:
            raise ValueError('Game has not started.')
        return time.time() - self.start_time

    def end_game(self):
        elapsed_time = self.get_elapsed_time()
        print(f'Game ended. Total time: {elapsed_time:.2f} seconds')

if __name__ == '__main__':
    game = Game()
    game.start_game()
    try:
        game.simulate_input('jump')
        print(f'Elapsed Time: {game.get_elapsed_time():.2f} seconds')
        game.simulate_input('fly')  # This will raise an error
    except ValueError as e:
        print(e)
    game.end_game()
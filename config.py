import json

DEFAULTS = {
    'screen_width': 1920,
    'screen_height': 1080,
    'fullscreen': False,
    'vsync': True,
    'sensitivity': 1.0
}

def load_config(file_path):
    try:
        with open(file_path, 'r') as config_file:
            user_config = json.load(config_file)
    except FileNotFoundError:
        user_config = {}
    return {**DEFAULTS, **user_config}

if __name__ == '__main__':
    config = load_config('config.json')
    print(config)
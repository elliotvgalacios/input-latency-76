import time
import requests

class NetworkError(Exception):
    pass

class Retry:
    def __init__(self, retries=3, delay=1, backoff=2):
        self.retries = retries
        self.delay = delay
        self.backoff = backoff

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < self.retries:
                try:
                    return func(*args, **kwargs)
                except requests.exceptions.RequestException:
                    attempts += 1
                    if attempts < self.retries:
                        time.sleep(self.delay)
                        self.delay *= self.backoff
                    else:
                        raise NetworkError('Max retries exceeded')
        return wrapper

@Retry(retries=5, delay=2)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
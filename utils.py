import time
import requests

def retry_request(url, retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise e

if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print(data)
    except Exception as e:
        print(f'Error occurred: {e}')
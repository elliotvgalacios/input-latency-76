import time

class InputLatencyTracker:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self):
        if self.start_time is None:
            raise ValueError('Timer was not started.')
        return time.perf_counter() - self.start_time

def calculate_average_latency(latencies):
    if not latencies:
        raise ValueError('Latencies list cannot be empty.')
    return sum(latencies) / len(latencies)

def is_latency_acceptable(latency, threshold):
    return latency <= threshold

def log_latency(latency):
    print(f'Latency: {latency:.4f} seconds')
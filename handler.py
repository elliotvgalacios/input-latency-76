import time
import numpy as np

def calculate_average_latency(latencies):
    return np.mean(latencies)


def is_latency_normal(latency, threshold=50):
    return latency <= threshold


def record_latency(latencies, new_latency):
    latencies.append(new_latency)
    if len(latencies) > 100:
        latencies.pop(0)


def calculate_variance(latencies):
    average = calculate_average_latency(latencies)
    variance = np.mean([(x - average) ** 2 for x in latencies])
    return variance


def format_latency(latency):
    return f'{latency:.2f} ms'


def log_latencies(latencies):
    for latency in latencies:
        print(format_latency(latency))

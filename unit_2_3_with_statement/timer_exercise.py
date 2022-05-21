'''
Implement a context manager that measures the execution time
of a code block using the time.time function.
Try both decorator-based and a class-based variant.
'''

from time import time
from contextlib import contextmanager

# Approach 1: Using __enter__ __exit__ interface
class Timer:
    def __init__(self):
        pass

    def __enter__(self):
        self.start_time = time() # returns the time in seconds since the epoch as float.
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        time_elapsed = time() - self.start_time
        print(f'Time Elapsed: {time_elapsed:.2f} seconds')


with Timer() as timer:
    for i in range(1000000):
        pass

# Approach 2: Using @contextmanager decorator
@contextmanager
def timer():
    try:
        start_time = time()
        yield start_time
    finally:
        time_elapsed = time() - start_time
        print(f'Time Elapsed: {time_elapsed:.2f} seconds')

with timer() as timer:
    for i in range(1000000):
        pass
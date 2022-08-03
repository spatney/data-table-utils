'''Time function execution'''
import time


def time_it(func,  *args, **kwargs):
    '''time_it'''
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time() - start_time
    return [result, end_time]

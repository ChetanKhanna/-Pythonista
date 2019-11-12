"""
Some clsoe to real-world decorators.

A good boiler-plate code for a real world decorator:

def decorator_name(func):
    @functools.wrap(func)
    def wrapper(*args, **kwargs):
        # Do someting before
        value = func(*args, **kwargs) # assuming func has a return val
        # Do something after
        return value
    return wrapper

"""

import functools
import timeit

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        exec_time = timeit.timeit(func(*args, **kwargs))
        print(f"Fininshed {func.__name__} in {exec_time: .4f} secs")
    return wrapper

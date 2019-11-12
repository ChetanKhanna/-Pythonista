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
import time

PLUGINS = {}

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f'Finished {func.__name__} in {end_time-start_time:4f} secs')
        return value
    return wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_list = [repr(a) for a in args]
        kwargs_list = [f'{k}={v}' for k, v in kwargs.items()]
        signature_list  = ', '.join(args_list + kwargs_list)
        print(f'Calling {func.__name__}({signature_list})')
        value = func(*args, **kwargs)
        print(f'{func.__name__} returned {value}')
        return value
    return wrapper

def register(func):
    """Registers a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

# The way it works:
# decorator("arg1", "arg2")(func)(*args, **kwargs)

def repeat(num_times=2):
    def decorator_func(func):
        @functools.wraps(functools)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator_func
    
# class based decorators
def singleton(cls):
    """
    To ensure that a class has only one instance all the time.
    This is frequently used in objects like None, True, False
    in Python
    """
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        print('inside wrapper')
        if not wrapper.instance:
            wrapper.instance = cls(*args, **kwargs)
        return wrapper.instance
    wrapper.instance = None
    return wrapper

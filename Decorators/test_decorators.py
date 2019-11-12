"""
This file is for testing and playing around with not-so-useful yet
simple to understand and dig around the decorators in python.
"""

import functools

# Decorator without an argument
def greetings(func):
    def wrapper(): # warpper is a convetinal name in a decorator
        func()
    return wrapper

def greet_twice(func):
    def wrapper():
        func()
        func()
    return wrapper

def greet_someone(func):
    def wrapper(name):
        func(name)
    return wrapper

def greet_someone_rudely(func):
    def wrapper(*args, **kwargs):
        print('I will not say hello to %s' %args[0])
    return wrapper

def test_decorated_func_ref(func):
    def wrapper(*args, **kwargs):
        print('This is from inside wrapper: ', func.__name__)
    return wrapper

def retain_decorated_func_ref(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        pass
    return wrapper

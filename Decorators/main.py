# importing requires modules
import argparse
import math
import functools
# importing decorators
from test_decorators import (greetings, greet_twice, greet_someone,
                        greet_someone_rudely, retain_decorated_func_ref,
                        test_decorated_func_ref)
from decorators import (PLUGINS, timer, debug, register, repeat, singleton,)


@greetings
def say_hello():
    print('Hey there! Hello :)')

@greet_twice
def say_hello_2():
    print('Hello there, have a nice day!')

@greet_someone
def hello_name(name):
    print('Hello, %s' %name)

@greet_someone_rudely
def no_hello(name):
    """
    In a way, the decorator replaced the decorated functino with
    `wrapper` defined inside decorator. So the `wrapper` may decide
    not to use the decorated function at all, as is the case here.
    """
    print('I wanted to say hello.. :(')

@timer
def counter():
    square_roots = []
    for _ in range(1000):
        square_roots.append(math.sqrt(_))
    return square_roots



@debug
def approximate_e(terms=10):
    return sum(1 / math.factorial(n) for n in range(terms))

@register
def just_a_func():
    pass

@register
def just_a_func_with_args(dummy_arg, dummy_kwarg=0):
    pass

# The way it works:
# repeat_n_times = repeat(num_times)(repeat_n_times)(name)
@repeat(num_times=4)
def repeat_n_times(name='Charles'):
    print(f'Hello, {name}')

# The way it works:
# class_obj = sigleton(ClassBaseDecorator)
@singleton
class ClassBasesDecorator:
    pass

@functools.lru_cache()
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num-2) + fibonacci(num-1)

##################### Execution ######################

# creating parser
parser = argparse.ArgumentParser(allow_abbrev=False)

parser.add_argument('module', metavar='Module', default='main',
                    help='Specify main or test to run either main or'
                    'test set of decorators')
args = parser.parse_args()

def test_main():
    say_hello()
    say_hello_2()
    hello_name('Bob')
    no_hello('Charlie')

def main():
    counter()
    print(approximate_e())
    print(approximate_e(5))
    just_a_func()
    just_a_func_with_args(10)
    print(PLUGINS)
    repeat_n_times('Marley')
    repeat_n_times()
    print('Creating first object')
    class_obj_1 = ClassBasesDecorator()
    print('Creating second object')
    class_obj_2 = ClassBasesDecorator()
    print(id(class_obj_1) == id(class_obj_2))
    print(class_obj_1, ' ', class_obj_2)
    print(fibonacci(10))


if __name__ == "__main__":
    if 'test' in args.module:
        test_main()
    else:
        main()

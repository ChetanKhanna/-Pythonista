# importing decorators
from test_decorators import (greetings, greet_twice, greet_someone,
                        greet_someone_rudely, retain_decorated_func_ref,
                        test_decorated_func_ref,)

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



def main():
    say_hello()
    say_hello_2()
    hello_name('Bob')
    no_hello('Charlie')

if __name__ == "__main__":
    main()

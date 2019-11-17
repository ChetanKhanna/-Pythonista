from contextlib import ContextDecorator, contextmanager

# standard method to create a context manager
# any class with __enter__ and __exit__ can act as
# a context manaer
class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, exc_type, exc_val, exc_traceback):
        """
        exc_type: class of Exception, eg, AttributeError
        exc_val: The value, usually the message of eception
        exc_traceback: traceback object refernce
        """
        self.open_file.close()

# using contextmanger from contextlib to turn
# functions into context managers
@contextmanager
def tag(name): # name of the tag, for example, <p>
    "The function must have one and only one `yield`"
    print(f'<{name}>')
    yield
    print(f'</{name}>')

# testing
with tag('Hello'):
    print('Smile!')

@tag('Hello')
def foo():
    print('Okay!')

foo()

# using ContextDecorator of contextlib to turn
# class into a contextmanager.
# This class can be used both as decorator and
# using `with` statement
class MakeParagraph(ContextDecorator):
    def __enter__(self):
        print('<p>')
        return self

    def __exit__(self, exc_type, exc_val, exc_traceback):
        print('</p>')


# testing
@MakeParagraph()
def make_para():
    print('Hello World')

make_para()

with MakeParagraph():
    print('Hello World 2')


# handling exceptions using context managers
class CM:
    def __init__(self):
        print('Inside __init__')
        self.init_var = 0

    def __enter__(self):
        print('inside __enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        If we return None or False, the exception will be raised.
        But returning true will not raise the exception that occured
        inside the with block below.
        """
        print('inside __exit__')
        if exc_type:
            print(exc_type)
            print(exc_val)
            print(exc_tb)
            return True

# testing
with CM() as cm:
    print('inside with')
    print(cm.init_var)
    raise Exception('Yo man')

# An example on a standard Python class
class SampleClass:
    pass

print(SampleClass.__name__, SampleClass.__bases__, SampleClass.__dict__)
# new classes via type() keyword
# type(<name>, <bases>, <dct>)
# <name>:: `str` : This is the output of SomeClass.__name__
# <bases>:: `tuple :` which becomes the __bases__ of the class
# <dct>:: `dict` : which becomes the __dict__ of the class
Foo = type('Foo', (), {})
print(Foo.__name__, Foo.__bases__, Foo.__dict__)

# Another example
Bar = type('Bar', (Foo,), {'attr': 100})

class ClassWithAttr:
   attr = 100


print(Bar.__name__, Bar.__bases__, Bar.__dict__)
print(ClassWithAttr.__name__, ClassWithAttr.__bases__, ClassWithAttr.__dict__)

########## Custom MetaClass ##########
class Meta(type):
    def __new__(cls, name, bases, dct):
        instance = super().__new__(cls, name, bases, dct)
        print('Hurray!')
        return instance

class Voodoo(metaclass=Meta):
    pass

class_instance = Voodoo()


# Implementing a Singleton class
class _Singleton(type):
    """
    A metaclass that forms the Singleton base class
    """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        """
        Remember here __call__ in that of a metaclass and therefore will
        be executed before __new__ and __init__ of the class (the __call__
        of actual class never get executed in our example)
        Dont confuse it with the order or execution of __new__ __init__
        and __call__ defined below for instance creation.
        MetaClasses are for class creation, analogous to as classes are for
        instance creation.
        """
        print('__call in _Singleton')
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=_Singleton):
    def __new__(cls, *args, **kwargs):
        print('__new__ in Singleton')
        return super(Singleton, cls).__new__(cls, *args, **kwargs)
    
    def __init__(self, *args, **kwargs):
        print('__init__ in Singleton')

    def __call__(self, *args, **kwargs):
        print('__call__ in Singleton')

# Testing for singleton class
first_obj = Singleton()
second_obj = Singleton()
print(first_obj == second_obj)
print(id(first_obj), id(second_obj))

# Understanding __call__, __new__ and __init__
"""
When class instance is executed (called like a function), __call__ in executed.
During object instantiation, first __new__ and then __init__ are called.
If __new__ returns the newly created instance of the class, i.e., by returning:
`instance = super(MyClass, cls).__new__(*args, **kwargs)`
`return instance`
If not, for eg. __new__ returns anything else, then an explicit call to __init__
before returning is necessary
"""

class TestClass:
    def __new__(cls, *args, **kwargs):
        print('__new__')
        return super(TestClass, cls).__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print('__init__')

    def __call__(self, *args, **kwargs):
        print('__call__')


# Testing
tc = TestClass()
tc()
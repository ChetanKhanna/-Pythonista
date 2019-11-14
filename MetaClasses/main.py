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


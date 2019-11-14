class DescriptorClass:
    variable = 100

    def __init__(self,  init_val=None, name='var'):
        self.val = init_val
        self.name = name

    def __get__(self, obj, objtype=None):
        """
        __get__ is called to get either an attribute of 
        the owner class or an object of that class.
        Hence when Descriptor() is called, Python returns
        the output of __get__ instead
        """
        print('Hello from __get__')
        # print(self, obj, objtype)
        # print(type(self), type(obj), type(objtype))
        return self.val 

    def __set__(self, obj, value):
        print('Hello from __set__')
        # print(self, obj, value)
        # print(type(self), type(obj), type(value))
        self.val = value


# set method raises AttributeError
class EncapsulationDescriptor:
    """
    This descriptor will raise AttributeError when
    the attribute's value is modified
    """

    def __init__(self, init_val=None, name='var'):
        self.val = init_val
        self.name = name

    def __get__(self, instance, owner_class=None):
        print('Hello from __get__')
        return self.val

    def __set__(self, instance, new_value):
        print('Hello from __set__')
        raise AttributeError('The value of this attribute cannot be changed!')

# using property function
class DescriptorClass2:
    """
    This class will use the descriptor of property()
    for defining getter and setter for its attribute
    """
    def __init__(self, x):
        self._x = x

    def getx(self):
        print('Hello from getx')
        return self._x

    def setx(self, value):
        print('Hello from setx')
        self._x = value

    # Attribute x
    x = property(getx, setx)


# using property decorator
class DescriptorClass3:
    """
    This class will use property decorator
    for defining getter and setter for its attribute
    """
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        print('Hello from getter')
        return self._x

    @x.setter
    def x(self, value):
        print('Hello from setter')
        self._x = value


class TestClass:
    x = 22
    y = DescriptorClass(10, 'y')
    z = EncapsulationDescriptor(42, 'z')



########## Execution Block ##########
def main():
    tc = TestClass()
    print(tc.x)
    tc.x = 29
    print(tc.x)
    print(tc.z)
    try:
        tc.z = 96
    except AttributeError as e:
        print(e)
    
    dc2 = DescriptorClass2(2)
    print(dc2.x)

    dc3 = DescriptorClass3(10)
    print(dc3.x)
    dc3.x = 12


if __name__ == "__main__":
    main()

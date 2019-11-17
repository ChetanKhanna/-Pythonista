class BaseClass:
    attr1 = 1
    def test_func(self):
        print('1st test func')


class Mixin1:
    attr2 = 2
    def test_func(self):
        print('2nd test func')

class Mixin2:
    attr3 = 3
    def test_func(self):
        print('3rd test func')


class MyClass(Mixin2, Mixin1, BaseClass): # check the order
    pass

# Testing
mcls = MyClass()
print(mcls.attr1, mcls.attr2, mcls.attr3)
mcls.test_func() # the last test func

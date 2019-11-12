"""
This file is intended to work out examples that
deal with standard decorators provided by Python
for methods in any class.
"""


class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @staticmethod
    def pi():
        """
        Can be used both as class method and an instance method.
        For eg.: c.pi() [c is an instance of class Circle, i.e., c = Circle(val)]
        and Circle.pi() both return the same value.
        They *DO NOT* recieve any implicit first argument, hence, no `self` or
        `cls` used; both of them are simply ignored
        """
        return 3.14

    @property
    def area(self):
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        return self.area * height
    
    @classmethod
    def unit_circle(cls):
        """
        Can be used both as class method and an instance method.
        For eg.: c.unnit_circle() [c is an instance of class Circle, i.e., c = Circle(val)]
        Remember cls and self are just conventions and doesn't matter if we replace them by
        something else as long as they are the first param in a method.
        However, unlike normal instance methods, what they store in this first parameter is
        the class and not the instane of class. If called with an instance, they simply take
        the class of the instance from it and ignore the rest.
        """
        return cls(1)
    

def main():
    c = Circle(5)
    print('Radius: ', c.radius)
    print('Area: ', c.area)
    c.radius = 10
    print('Radius: ', c.radius)
    print('Area: ', c.area)
    try:
        c.area = 100
    except AttributeError:
        print('Cannot change area as it has no setter defined'
               'exclusively')
    print('Cyclinder_volume: ', c.cylinder_volume(10))
    try:
        c.radius = -1
    except ValueError as e:
        print(e)
    uc = Circle.unit_circle()
    print(uc)
    try:
        uc = c.unit_circle()
        print(uc)
    except Exception as e:
        print(e)
    print('Instance: ', c.pi())
    print('Class: ', Circle.pi())

if __name__ == "__main__":
    main()

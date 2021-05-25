from math import *

# multiple coordinate systems example
# using a single __init__ to define both cartesian and polar

'''
solution 1 : enum for 2 factories
define __init__(a, b, system=cartesian):
if system == cartesian:
    x = a
    y = b
else:
    x = a * cos(b)
    y = b * sin(b)

inconvenient if we add more ...
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'x: {self.x}, y: {self.y}'
        
    @staticmethod
    def new_cartesian(x, y):
        return Point(x, y)
    
    @staticmethod
    def new_polar(rho, theta):
        return Point(rho*cos(theta), rho*sin(theta))
        
if __name__ == "__main__":
    p = Point(2, 3)
    p2 = Point.new_polar(1, 2)
    print(p)
    print(p2)
    
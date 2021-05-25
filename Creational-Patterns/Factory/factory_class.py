from math import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'x: {self.x}, y: {self.y}'
     
    # Factory class
    class PointFactory:   
        # methods need not be static
        # add self when they are not static
        def new_cartesian(self, x, y):
            return Point(x, y)
        
        def new_polar(self, rho, theta):
            return Point(rho*cos(theta), rho*sin(theta))
    
    # singleton instance -> point as 1 single static factory
    factory = PointFactory()
        
if __name__ == "__main__":
    p = Point(2,3)
    p2 = Point.factory.new_polar(1,2)
    print(p)
    print(p2)
    
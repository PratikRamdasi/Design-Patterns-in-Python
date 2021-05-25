from abc import ABC

class Shape(ABC):
    def __str__(self):
        return ''
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f'A circle of radius {self.radius}'

class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def __str__(self):
        return f'A square with side {self.side}'


class ColoredShape(Shape):
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def resize(self, factor):
        # note that a Square doesn't have resize()
        r = getattr(self.shape, 'resize', None)
        if callable(r):
            self.shape.resize(factor)

    def __getattr__(self, item):
        return getattr(self.__dict__['shape'], item)

    def __str__(self):
        return f'{self.shape} has the color {self.color}'
    
circle = ColoredShape(Circle(5), 'red')
print(circle)

circle.resize(2)
print(circle)

sq = ColoredShape(Square(5), 'blue')
print(sq)

sq.resize(2)
print(q)
from abc import ABC

# Augment functionality of the class.

class Shape(ABC):
    def __str__(self):
        return ''

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f'A circle with radius {self.radius}'

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'A Square with side {self.side}'

# decorator class with additional color info
class ColoredShape(Shape):
    def __init__(self, shape, color):
        # solution - 
        # if isinstance(shape, ColoredShape):
        #     raise Exception('Can not apply same operation twice')
        self.shape = shape
        self.color = color

    # def resize ...

    def __str__(self):
        return f'{self.shape} has color {self.color}'

if __name__ == "__main__":
    circle = Circle(2)
    print(circle) # A circle with radius 2

    red_circle = ColoredShape(circle, 'red')
    ## NOTE: Not possible to call resize method for red_circle 
    # because  ColoredShape is not a circle 
    # red_circle.resize(3) #### THROWS an ERROR
    ## Solution -> `Dynamic Decorator`
    print(red_circle) # A circle with radius 2 has color red

    #  Disadvantage -> it is possible to use the decorator multiple times 
    mixed = ColoredShape(ColoredShape(Square(3), 'red'), 'green')
    print(mixed) # A Square with side 3 has color red has color green -> ERROR
    # solution - raise exception in ColoredShape class if the instance is repeated

    # overall - its possible to do Colored(Colored(Transparent(Colored(shape)))) etc ...


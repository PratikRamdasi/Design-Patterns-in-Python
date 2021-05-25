class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property   
    def area(self):
        return self._height * self._width
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value
        
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value

# derived class        
class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)
    
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value
        
    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value
    
def use_it(rc):
    w = rc.width
    rc.height = 10
    ex = int(w * 10)
    print(f'Expected:{ex}, got:{rc.area}')
    
rc = Rectangle(2, 3)
use_it(rc)

# use_it does not work on derived class, Violation of LSP 
sq = Square(5)
use_it(sq)
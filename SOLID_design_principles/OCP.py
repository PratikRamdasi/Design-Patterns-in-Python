# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    
class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
        
class Specification:
    def is_satisfied(self, item):
        pass
    
    # overload binary & operator
    def __and__(self, other):
        return AndSpecification(self, other)
    
    # overload OR operator
    def __or__(self ,other):    
        return ORSpecification(self, other)

class Filter:
    def filter(self, items, spec):
        pass
    
class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color
        
    def is_satisfied(self, item):
        return item.color == self.color
            
class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size
        
    def is_satisfied(self, item):
        return item.size == self.size

class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args
        
    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))
        
class ORSpecification(Specification):
    def __init__(self, *args):
        self.args = args
        
    def is_satisfied(self, item):
        return any(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item
  
if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.MEDIUM)
    house = Product('House', Color.BLUE, Size.LARGE)
    
    products = [apple, tree, house]
    
    bf = BetterFilter()
    print('Green products: ')
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(p.name)
        
    print('Large products: ')
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(p.name)
        
    print('Green and Small products: ')
    # overloaded & operator 
    green_small = green & SizeSpecification(Size.SMALL)
    for p in bf.filter(products, green_small):
        print(p.name)
        
    print('Blue or Medium products: ')
    # overloaded | operator 
    blue_med =ColorSpecification(Color.BLUE) | SizeSpecification(Size.MEDIUM)
    for p in bf.filter(products, blue_med):
        print(p.name)

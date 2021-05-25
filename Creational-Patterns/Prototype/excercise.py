import copy

class Point: # address
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'x:{self.x}, y:{self.y}'

class Line: # person
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        # define new start and end points
        new_start = Point(self.start.x, self.start.y)
        new_end = Point(self.end.x, self.end.y)
        return Line(new_start, new_end)
        
    def __str__(self):
        return f'Start: {self.start}, end: {self.end}'

start = Point(4, 5)
end = Point(6, 7)
print(start)
print(end)
L = Line(start, end)
print(L)

L1 = L.deep_copy()
L1.start.x = 10
L1.end.y = 11
print(L1)

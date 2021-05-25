class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def draw_point(p):
    print('.', end='')
    
# ^^ given API
# 
# TODO: Rectangles class   

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


# Improvements: use CACHING
# its no longer just a list, but we need to iterate on cache
class LineToPointAdapter: # (list):
    cache = {}

    def __init__(self, line):
        # compute hash of line(list of points) already stored in cache
        self.h = hash(line)
        if self.h in self.cache:
            return

        super().__init__()

        print('Generating points for line '
              f'[{line.start.x}, {line.start.y}]->', 
              f'[{line.end.x}, {line.end.y}]')

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.y)

        # don't append to self, instead make new list
        points = []

        if right - left == 0:
            for y in range(top, bottom):
                points.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                points.append(Point(x, top))

        self.cache[self.h] = points

    # iterate over cache
    def __iter__(self):
        return iter(self.cache[self.h])



## We need adapter from line to point
## IMP : Line represented as points
'''
class LineToPointAdapter(list):
    # it will be list of points
    # we will be generaing lots of points
    count = 0 # to count number of points

    def __init__(self, line):
        super().__init__()
        self.count += 1 # keep track of generated points

        print(f'{self.count}: Generating points for line '
              f'[{line.start.x}, {line.start.y}]->', 
              f'[{line.end.x}, {line.end.y}]')

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.y)

        if right - left == 0:
            for y in range(top, bottom):
                self.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                self.append(Point(x, top))
'''

def draw(rcs):
    print('---- drawing stuff ----')
    for rc in rcs:
        for line in rc:
            ## we need draw_line interface here 
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)

if __name__ == '__main__':
    rcs = [
        Rectangle(1,1,10,10),
        Rectangle(3,3,6,6)
    ]
    draw(rcs)
    
    # Adapter Generates points again -> temporary objects
    ## IMP : NEED for CACHING
    # draw(rcs) 

    # after Caching
    draw(rcs)
    draw(rcs)  # prints points only once

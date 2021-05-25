
## CONTAINER for other objects

class GraphicObject:
    # serve single shapes like - circle, square
    # and groups of shapes - group(circle, square)
    def __init__(self, color=None):
        self.color = color
        self.children = []
        self._name = 'Group'

    @property
    def name(self):
        return self._name

    # utility method to print(draw) the shapes
    def _print(self, items, depth):
        items.append('*' * depth)
        if self.color:
            items.append(self.color)
        items.append(f'{self.name}\n')

        for child in self.children:
            child._print(items, depth + 1)

    # goal - DRAW graphic object
    def __str__(self):
        items = []
        self._print(items, 0)
        return ''.join(items)


class Circle(GraphicObject):
    @property
    def name(self):
        return 'Circle'


class Square(GraphicObject):
    @property
    def name(self):
        return 'Square'

if __name__ == "__main__":
    drawing = GraphicObject()
    drawing._name = 'My drawing'
    drawing.children.append(Circle('Yellow'))
    drawing.children.append(Square('Red'))

    group = GraphicObject()
    group.children.append(Circle('Blue'))
    group.children.append(Square('Blue'))
    drawing.children.append(group)

    print(drawing)
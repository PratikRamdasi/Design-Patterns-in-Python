## Drawing application -> 
# circle square 
# vector raster  --> different forms they can be drawn

# need 4 classes  
# vectorCircle, vectorSq, rasterCircle, rasterSq 
## but this is not scalable -> complexity increases with addition of new shape
## goal - reduce number of objects
## idea - split content within different renderers and shapes
## make connection between shapes and renderers

## BREAKS OCP -> rendered is tied directly to object(circle), if we introduce
# triangle, we need to add render_triangle method in every renderer class

from abc import ABC

class Renderer(ABC):
    def render_circle(self, radius):
        pass
    def render_square(self):
        pass

# define two renderers
class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'drawing circle with radius: {radius}')

class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'drawing pixels for a circle with radius: {radius}')

# heirarchy of shapes -> BRIDGE 
class Shape:
    def __init__(self, renderer): # IMP - this connects the renderer with shape
        self.renderer = renderer

    def draw(self): pass
    def resize(self, factor): pass

class Circle(Shape):
    def __init__(self, renderer, radius):
        # init the renderer for this shape
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor 



if __name__ == "__main__":
    raster = RasterRenderer()
    vector = VectorRenderer() 
    circle = Circle(vector, 5) # Circle(raster, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()


    


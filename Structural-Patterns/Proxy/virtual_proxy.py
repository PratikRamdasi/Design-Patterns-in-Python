# application - manage peoples photos 
# Bitmaps of images you are storing

class Bitmap:
    # gets loaded from filename
    def __init__(self, filename):
        self.filename = filename
        print(f'Loading image from {self.filename}')
    
    # draw the image
    def draw(self):
        print(f'Drawing image {self.filename}')

# Virtual Proxy
class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None # only assign in draw state

    def draw(self):
        # init if bitmap is not set == None
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()

def draw_image(image):
    # adds additional diagnostic
    print('About to draw image')
    image.draw()
    print('Done drawing the image')


if __name__ == "__main__":
    bmp = Bitmap('facepalm.jpg')
    # draw_image(bmp) --> problem

    # Problem : Event if we don't draw the image, it will still load the image 
    # this can be expensive
    # sol1 : load the image inside draw -> violates OCP
    # 
    # sol2 :  VirtualProxy -> lazy loading of the image
    # check class LazyBitmap 
    # Loads the image ONLY ONCE at first invocation

    bmp1 = LazyBitmap('facepalm.jpg')
    draw_image(bmp1)

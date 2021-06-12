# building a console -> buffers, viewports
# -> buffers are the memory chunk where characters are stored
# -> viewports give the view of those buffers
# Console -> high level class, Facade

# store list of chars into buffer
class Buffer:
    # can be 2 or 1D chunk of memory
    def __init__(self, width=30, height=20):
        self.width = width
        self.height = height
        self.buffer = [' '] * (width * height)
    
    # write to buffer
    def write(self, text):
        self.buffer += text

    # support for chat at index
    def __getitem__(self, item):
        return self.buffer.__getitem__(item)

# shows chunk of buffer on a screen somewhere
class Viewport:
    def __init__(self, buffer=Buffer()):
        self.buffer = buffer
        self.offset = 0

    # get char at specific location
    def get_char_at(self, index):
        return self.buffer[index + self.offset]

    # append text to buffer
    def append(self, text):
        self.buffer.write(text)

# high level -> Facade
# HIDE the complexity
# Both high level and low level can be easily accessible
class Console:
    def __init__(self):
        # setup default buffer and default viewport for that buffer
        # both of them can be [lists], somebody working on low level
        # can add buffer and viewport
        b = Buffer()
        self.current_viewport = Viewport(b)
        self.buffers = [b]
        self.viewports = [self.current_viewport]

    # can provide both high level and low level methods
    # high level
    def write(self, text):
        self.current_viewport.buffer.write(text)

    # expose low level methods
    def get_char_at(self, index):
        return self.current_viewport.get_char_at(index)

if __name__ == "__main__":
    c = Console()
    c.write('hello') # use high level API
    c.get_char_at(0) # use low level API

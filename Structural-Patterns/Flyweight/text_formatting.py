# capitlize certain letters in plain text
# how to decide which letters to capitalize ?
# => Idea1: bool array with same length as plain_text
#           -> set the required letters (positions) to True 
# specify letters -> use range (start, end) position

class FormattedText:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        ## NOTE:
        # storing all bool values of size of text
        # which is not needed
        self.caps = [False] * len(plain_text)

    # set the positions for letters to capitalize to True
    def capitalize(self, start, end):
        for i in range(start, end):
            self.caps[i] = True

    def __str__(self):
        result = []
        # generate capitalized string
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            result.append(
                c.upper() if self.caps[i] else c
            )
        return ''.join(result)

class BetterFormattedText:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.formatting = []

    # FLYWEIGHT class
    # works on range of chars and applies some operation to them
    class TextRange:
        def __init__(self, start, end, capitalize=False):
            self.start = start
            self.end = end
            self.capitalize = capitalize

        # check if given position is in between start, end
        def covers(self, pos):
            return self.start <= pos <= self.end

    # getting range and add to formatting
    def get_range(self, start, end):
        range = self.TextRange(start, end)
        self.formatting.append(range)
        return range # in order to add more formatting after returning

    def __str__(self):
        result = []

        # for every position in text
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            for r in self.formatting:
                # check if this pos is covered by formatting
                # for ex. if this letter needs to be capitalized
                if r.covers(i) and r.capitalize:
                    c = c.upper()
            result.append(c)

        return ''.join(result)


if __name__ == "__main__":
    
    text = 'This is a brave new world'
    ft = FormattedText(text)

    ft.capitalize(10, 15)
    print(ft) # This is a BRAVE new world

    ## we don't need bool array with size(text), 
    # use flyweight pattern instead
    bft = BetterFormattedText(text)
    bft.get_range(16, 19).capitalize = True
    print(bft) # This is a brave NEW world



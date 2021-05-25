# text processor - Process elements and output them 
# either as Markdown or HTML 
# Elements are in list format
from abc import ABC
from enum import Enum

class ListStrategy(ABC):
    def start(self, buffer): pass
    def end(self, buffer): pass
    def add_list_item(self, buffer, item): pass
        # adds element to the buffer

class MarkdownStrategy(ListStrategy):
    # no need for start and end
    def add_list_item(self, buffer, item):
        buffer.append(f'  * {item}\n')

class HTMLStrategy(ListStrategy):
    def start(self, buffer):
        buffer.append('<ul>\n')

    def end(self, buffer):
        buffer.append('</ul>\n')

    # no need for start and end
    def add_list_item(self, buffer, item):
        buffer.append(f'  <li>{item}</li>\n')

class OutputFormat(Enum):
    MARKDOWN = 1
    HTML = 2

class TextProcessor:
    def __init__(self, list_strategy=HTMLStrategy()): # default
        self.list_strategy = list_strategy
        self.buffer = [] # list of listelement

    # uses list strat to perform operations
    def append_list(self, items):
        # add list elements to buffer in specific format
        # define listStrategy to process list
        ls = self.list_strategy
        ls.start(self.buffer) 
        for item in items:
            ls.add_list_item(self.buffer, item)
        ls.end(self.buffer)

    # change strategy at runtime
    def set_output_format(self, format):
        if format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdownStrategy()
        elif format == OutputFormat.HTML:
            self.list_strategy = HTMLStrategy()

    def __str__(self):
        return ''.join(self.buffer)

    def clear(self):
        self.buffer.clear()

if __name__ == "__main__":
    items = ['foo', 'bar', 'baz']

    tp = TextProcessor()
    tp.set_output_format(OutputFormat.MARKDOWN)
    tp.append_list(items)
    print(tp)

    # change format
    tp.set_output_format(OutputFormat.HTML)
    tp.clear()
    tp.append_list(items)
    print(tp)

    '''
    * foo
    * bar
    * baz

    <ul>
        <li>foo</li>
        <li>bar</li>
        <li>baz</li>
    </ul>
    '''


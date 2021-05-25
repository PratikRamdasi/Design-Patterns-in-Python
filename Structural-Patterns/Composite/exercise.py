from abc import ABC
from collections.abc import Iterable
import unittest

class ValueContainer(Iterable, ABC):
    # object can be iter [[]] collection or list
    def sum(self):
        result = 0
        for s in self: # type of object
            for i in s:
                result += i
        return result

class SingleValue(ValueContainer):
    def __init__(self, value):
        self.value = value
    
    def __iter__(self):
        yield self.value

class ManyValues(list, ValueContainer):
    pass


class FirstTestSuite(unittest.TestCase):
    def test(self):
        svalue = SingleValue(11)
        othervalues = ManyValues()
        othervalues.append(22)
        othervalues.append(33)

        allvalues = ManyValues()
        allvalues.append(svalue)
        allvalues.append(othervalues)

        self.assertEqual(allvalues.sum, 66)

import re
from enum import Enum

class ExpressionProcessor:
    class NextOp(Enum):
        PLUS = 1
        MINUS = 2

    def __init__(self):
        self.variables = {}

    def calculate(self, expression):
        current = 0
        next_op = None

        parts = re.split('(?<=[+-])', expression)

        for p in parts:
            temp = re.split('[\+\-]', p)
            first = temp[0]
            try:
                value = int(first)
            except ValueError:
                if len(first) == 1 and first[0] in self.variables:
                    value = self.variables[first[0]]
                else:
                    return 0
            
            if not next_op:
                current = value
            elif next_op = self.NextOp.PLUS:
                current += value
            elif next_op = self.NextOp.MINUS:
                current -= value

            if p.endswith('+'):
                next_op = self.NextOp.PLUS
            elif p.endswith('-'):
                next_op = self.NextOp.MINUS

        return current


        
# Better implementation 
# -> separate class for printing
from abc import ABC

class Expression(ABC):
    pass

class DoubleExpression(Expression):
    def __init__(self, value):
        self.value = value


class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.right = right
        self.left = left


# separate class provides better implementation
# GOOD -> separation of concerns -> SOC 
# BAD -> If new expression added (subtraction) then print
    # needs to be explicitly updated with elif to make e.print
    # work properly [code (print) will still run without elif ]

class ExpressionPrinter(Expression):
    @staticmethod
    def print(e, buffer):
        # e can be AdditionExpression or DoubleExpression
        # checking -> reflection printer 
        if isinstance(e, DoubleExpression):
            buffer.append(str(e.value))
        elif isinstance(e, AdditionExpression):
            buffer.append('(')
            ExpressionPrinter.print(e.left, buffer)
            buffer.append('+')
            ExpressionPrinter.print(e.right, buffer)
            buffer.append(')')

    # giving functionality for call -> e.print(buffer)
    Expression.print = lambda self, b:\
        ExpressionPrinter.print(self, b)


if __name__ == "__main__":
    # expression - 1 + (2 + 3)
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )

    buffer = []
    e.print(buffer)
    # ExpressionPrinter.print(e, buffer)
    print(''.join(buffer)) # (1+(2+3)) 

    # adding another operation == evaluate an expression
    # print("ans = ", e.eval()) #ans =  6

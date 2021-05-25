# Intrusive -> direct, every class is modified with new
# operation to be done
# NOTE => Violates OCP 

# For ex : class DoubleExpression and class AdditionExpression
# both will implement 'evaluate' or 'print' for an expression

# For a very large hierarchy -> impractical to modify all classes

class DoubleExpression:
    def __init__(self, value):
        self.value = value

    # visitor -> buffer
    def print(self, buffer):
        buffer.append(str(self.value))

    def eval(self):
        return self.value

class AdditionExpression:
    def __init__(self, left, right):
        self.right = right
        self.left = left

    # visitor -> buffer
    def print(self, buffer):
        buffer.append('(')
        self.left.print(buffer)
        buffer.append('+')
        self.right.print(buffer)
        buffer.append(')')

    def eval(self):
        return self.left.eval() + self.right.eval()

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
    print(''.join(buffer)) # (1+(2+3))

    # adding another operation == evaluate an expression
    print("ans = ", e.eval()) #ans =  6

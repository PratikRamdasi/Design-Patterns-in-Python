# Evaluate numerical expression
from enum import Enum, auto

class Token:
    # Token can be anything - numeric INT value or brackets
    class Type(Enum):
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        LPAREN = auto() # left paranthesis
        RPAREN = auto() # right paranthesis

    def __init__(self, type, text):
        # takes the type of token and associated text with it 
        # (for printing the text mainly) 
        self.type = type
        self.text = text 

    def __str__(self):
        return f'`{self.text}`' # see whitespace by using ` ` 


def lex(input):
    # input is a string
    result = []

    i = 0
    while(i < len(input)):
        # check every char - 1 char
        if input[i] == '+':
            result.append(Token(Token.Type.PLUS, '+'))
        elif input[i] == '-':
            result.append(Token(Token.Type.MINUS, '-'))
        elif input[i] == '(':
            result.append(Token(Token.Type.LPAREN, '('))
        elif input[i] == ')':
            result.append(Token(Token.Type.RPAREN, ')'))
        # integer - more than 1 char
        else:
            digits = [input[i]]
            for j in range(i+1, len(input)):
                if input[j].isdigit():
                    digits.append(input[j])
                    i += 1
                else:
                    # digit parsing done, generate token for it -> 13, 4, 12, 1
                    result.append(Token(Token.Type.INTEGER, ''.join(digits)))
                    break
        i += 1
        
    return result

## Parsing ##
# takes tokens and returns objcect oriented structure

# integer object
class Integer:
    def __init__(self, value):
        self.value = value

# binary expression -> +, - etc
class BinaryExpression:
    class Type(Enum):
        ADDITION = 0
        SUBTRACTION = 1

    def __init__(self):
        self.type = None
        self.left = None # left side of expression
        self.right = None # right side of expression

    # calculate value of expression
    @property
    def value(self):
        if self.type == self.Type.ADDITION:
            return self.left.value + self.right.value
        else:
            return self.left.value - self.right.value

# Assume final expression is always binary expression
def parse(tokens):
    result  = BinaryExpression()
    # flag to put at LHS or RHS 
    have_lhs = False
    i = 0

    while i < len(tokens):
        token = tokens[i]

        if token.type == Token.Type.INTEGER:
            # put integer value into Integer object defined above
            integer = Integer(int(token.text))
            if not have_lhs:
                result.left = integer
                have_lhs = True
            else:
                result.right = integer

        elif token.type == Token.Type.PLUS:
            # modify current binary expression
            result.type = BinaryExpression.Type.ADDITION

        elif token.type == Token.Type.MINUS:
            # modify current binary expression
            result.type = BinaryExpression.Type.SUBTRACTION

        # open and close paranthesis
        # need to get sub expression and assign at proper left/right location
        elif token.type == Token.Type.LPAREN:
            # find right paranthesis to get the subex
            j = i
            while j < len(tokens):
                if tokens[j].type == Token.Type.RPAREN:
                    break
                j += 1
            subexpression = tokens[i+1:j]
            # parse subexpression recursively
            element = parse(subexpression)
            if not have_lhs:
                result.left = element
                have_lhs = True
            else:
                result.right = element
            
            i = j # to the starting of next subexpression
        
        i += 1

    return result

def calc(input):
    # split input into tokens
    tokens = lex(input)
    # turn tokens as string
    print(' '.join(map(str, tokens)))

    # parse the tokens
    parsed = parse(tokens)

    # print final result
    print(f'{input} = {parsed.value}')

if __name__ == "__main__":
    calc('(13+4)-(12+1)') # 4

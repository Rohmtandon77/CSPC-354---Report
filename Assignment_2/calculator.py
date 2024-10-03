
from lark import Lark, Transformer, v_args
import math

# Load grammar from external file
grammar = open("/Users/rohmtandon/Desktop/CPSC_Courses/CPSC_354/Assignment_2/grammar.lark").read()

# Initialize parser with the provided grammar
parser = Lark(grammar, parser='lalr')

# Transformer to walk the AST and evaluate the expression
class CalculateTree(Transformer):

    def _eval(self, node):
        """ Helper method to ensure all tree nodes are evaluated """
        if isinstance(node, (int, float)):  # check if already a number
            return node
        return self.transform(node)  # recursively evaluate sub-trees

    @v_args(inline=True)
    def add(self, a, b):
        return self._eval(a) + self._eval(b)

    @v_args(inline=True)
    def sub(self, a, b):
        return self._eval(a) - self._eval(b)

    @v_args(inline=True)
    def mul(self, a, b):
        return self._eval(a) * self._eval(b)

    @v_args(inline=True)
    def pow(self, a, b):
        return self._eval(a) ** self._eval(b)

    @v_args(inline=True)
    def neg(self, a):
        return -self._eval(a)

    @v_args(inline=True)
    def log(self, a, b):
        return math.log(self._eval(a), self._eval(b))

    @v_args(inline=True)
    def number(self, n):
        return int(n)  # convert Lark's token for a number into an integer

# Function to parse and evaluate the expression
def evaluate_expression(expression):
    tree = parser.parse(expression)  # parse the expression into a tree
    calc = CalculateTree()  # initialize the transformer
    return calc.transform(tree)  # evaluate and return the result

# Test example
if __name__ == '__main__':
    expression = "log 100 base 10 + 2 * (3 + 5)"
    result = evaluate_expression(expression)
    print(f"Result of the expression '{expression}' is: {result}")

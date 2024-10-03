
from lark import Lark, Transformer, v_args
import math

grammar = """

?start: exp
?exp: exp "+" exp   -> add
    | exp "*" exp   -> multiply
    | exp "^" exp   -> power
    | exp "-" exp   -> subtract
    | "-" exp       -> negate
    | "log" exp "base" exp -> log
    | "(" exp ")"   -> parenthesis
    | NUMBER        -> number

%import common.NUMBER
%ignore " "
"""

class CalculateTree(Transformer):
    @v_args(inline=True)
    def number(self, n):
        return int(n)

    @v_args(inline=True)
    def add(self, left, right):
        return left + right

    @v_args(inline=True)
    def multiply(self, left, right):
        return left * right

    @v_args(inline=True)
    def power(self, left, right):
        return left ** right

    @v_args(inline=True)
    def subtract(self, left, right):
        return left - right

    @v_args(inline=True)
    def negate(self, n):
        return -n

    @v_args(inline=True)
    def log(self, base, value):
        return math.log(value, base)

    @v_args(inline=True)
    def parenthesis(self, n):
        return n

def main():
    parser = Lark(grammar, parser='lalr', transformer=CalculateTree())
    expression = input("Enter an expression: ")
    result = parser.parse(expression)
    print("Result:", result)

if __name__ == "__main__":
    main()

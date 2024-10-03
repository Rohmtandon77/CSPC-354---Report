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
    number = int

    def add(self, args):
        return args[0] + args[1]

    def multiply(self, args):
        return args[0] * args[1]

    def power(self, args):
        return args[0] ** args[1]

    def subtract(self, args):
        return args[0] - args[1]

    def negate(self, args):
        return -args[0]

    def log(self, args):
        return math.log(args[0], args[1])

    def parenthesis(self, args):
        return args[0]

def main():
    parser = Lark(grammar, parser='lalr', transformer=CalculateTree())
    expression = input("Enter an expression: ")
    result = parser.parse(expression)
    print("Result:", result)

if __name__ == "__main__":
    main()

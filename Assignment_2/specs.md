
This program utilizes the Lark library to parse mathematical expressions based on a predefined grammar and then evaluates these expressions using a custom transformer class. The grammar is defined using Lark's syntax and should be fairly self-explanatory. 
As for the python program - The script is structured into two main parts: the CalculateTree transformer class and the main() function.

The transformer class inherits from Lark's Transformer class and defines methods for transforming the parse tree into a result. Each method corresponds to a rule in the grammar:
- number(self, n): Converts the parsed number into an integer.
- add(self, left, right): Returns the sum of two expressions.
-  multiply(self, left, right): Returns the product of two expressions.
- power(self, left, right): Returns the result of raising the first expression to the power of the second.
- subtract(self, left, right): Returns the difference between two expressions.
- negate(self, n): Returns the negation of the expression.
- log(self, base, value): Computes the logarithm of value with the specified base.
- parenthesis(self, n): Simply returns the expression inside the parentheses.

The main() function handles user input and interaction:
- It initializes a Lark parser with the specified grammar and the CalculateTree transformer.
- It prompts the user to enter an expression.
- It parses the expression using the parser and prints the result.

The Program Flow is fairly simple as follows
- Input: The user inputs a mathematical expression.
- Parsing: The Lark parser processes the input based on the specified grammar, constructing a parse tree.
- Transformation: The CalculateTree transformer processes the parse tree, recursively evaluating each node based on the defined transformation methods.
- Output: The result of the expression is printed.
import re

def evaluate_expression(expression):
    def compute(op, left, right):
        if op == '+':
            return left + right
        elif op == '*':
            return left * right
        elif op == '^':
            return left ** right

    if expression.isdigit():
        return int(expression)

    while '(' in expression:
        #Replace the innermost parentheses with result
        expression = re.sub(r'\(([^()]+)\)', lambda m: str(evaluate_expression(m.group(1))), expression)

    for op in ['^', '*', '+']:
        #Find a pattern matching simple binary operations with the operator from above
        while re.search(r'\d+' + re.escape(op) + r'\d+', expression):
            #Using regex to isolate parts of the expression
            pattern = r'(\d+)' + re.escape(op) + r'(\d+)'
            expression = re.sub(pattern, lambda m: str(compute(op, int(m.group(1)), int(m.group(2)))), expression)

    return int(expression)

expr = input("Enter an expression: ")
result = evaluate_expression(expr)
print(f"The result of the expression '{expr}' is: {result}")

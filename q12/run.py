import re

# Function to define operator precedence
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

# Function to convert infix expression to postfix notation
def infix_to_postfix(tokens):
    output = []
    stack = []
    for token in tokens:
        if token.isalnum() or re.match(r'^\d+(\.\d+)?$', token):  # operand (number or variable)
            output.append(token)
        elif token == '(':  # open parenthesis
            stack.append(token)
        elif token == ')':  # closing parenthesis
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # pop '('
        else:  # operator
            while stack and precedence(stack[-1]) >= precedence(token):
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return output

# Function to generate TAC (Three Address Code), quadruples, and triples from an expression
def generate_TAC_and_intermediate(expr):
    temp_count = 1
    tac = []
    quadruples = []
    triples = []

    # Remove semicolon and split the expression into tokens
    expr = expr.replace(";", "")
    tokens = expr.split()

    # If there's no '=', it's an invalid expression
    if "=" not in tokens:
        print(f"Invalid expression. It must contain '='.")
        return [], [], []

    lhs = tokens[0]  # Left-hand side (variable)
    rhs_tokens = tokens[2:]  # Right-hand side of the equation

    # Convert infix to postfix for the right-hand side expression
    postfix = infix_to_postfix(rhs_tokens)

    stack = []
    for token in postfix:
        if token.isalnum():  # operand (either variable or number)
            stack.append(token)
        else:  # operator
            if len(stack) < 2:
                print(f"Error: Not enough operands for operation {token}")
                return [], [], []
            op2 = stack.pop()
            op1 = stack.pop()
            temp = f"t{temp_count}"
            tac.append(f"{temp} = {op1} {token} {op2}")
            quadruples.append([token, op1, op2, temp])
            triples.append([token, op1, op2])
            stack.append(temp)
            temp_count += 1

    tac.append(f"{lhs} = {stack.pop()}")

    return tac, quadruples, triples

# Function to process multiple input expressions
def process_input():
    # Taking multi-line input until the user enters 'END' or presses Enter
    expressions = []
    print("Enter expressions (each on a new line). Type 'END' to finish input:")

    while True:
        expr = input()
        if expr.strip().upper() == "END":
            break
        expressions.append(expr.strip())

    output = {}

    # Process each expression
    for expr in expressions:
        tac, quadruples, triples = generate_TAC_and_intermediate(expr)
        output[expr] = {
            "Three Address Code": tac,
            "Quadruples": quadruples,
            "Triples": triples
        }

    return output

# Main program to execute the logic
results = process_input()

# Display results for each expression
for expr, result in results.items():
    print(f"\nFor the expression: {expr}")
    print("\nThree Address Code:")
    for line in result["Three Address Code"]:
        print(line)
    
    print("\nQuadruples:")
    for quad in result["Quadruples"]:
        print(quad)

    print("\nTriples:")
    for trip in result["Triples"]:
        print(trip)

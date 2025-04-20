def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def infix_to_postfix(tokens):
    output = []
    stack = []
    for token in tokens:
        if token.isalnum():  # operand
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
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

def generate_TAC(expr):
    temp_count = 1
    tac = []

    # Tokenize input
    expr = expr.replace("=", " = ")
    tokens = expr.split()

    if "=" not in tokens:
        print("Invalid expression. It must contain '='.")
        return []

    lhs = tokens[0]
    rhs_tokens = tokens[2:]

    # Convert infix to postfix
    postfix = infix_to_postfix(rhs_tokens)

    # TAC generation from postfix
    stack = []
    for token in postfix:
        if token.isalnum():
            stack.append(token)
        else:  # operator
            op2 = stack.pop()
            op1 = stack.pop()
            temp = f"t{temp_count}"
            tac.append(f"{temp} = {op1} {token} {op2}")
            stack.append(temp)
            temp_count += 1

    tac.append(f"{lhs} = {stack.pop()}")
    return tac

# 👉 User Input
user_expr = input("Enter an expression (e.g., a = (b + c) * (d - e)): ")
tac_output = generate_TAC(user_expr)

print("\nThree Address Code:")
for line in tac_output:
    print(line)

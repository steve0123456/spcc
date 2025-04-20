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
        if token.isalnum():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(token):
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return output

def generate_TAC_Quads_Triples(expr):
    temp_count = 1
    tac = []
    quads = []
    triples = []

    expr = expr.replace("=", " = ")
    tokens = expr.split()

    if "=" not in tokens:
        print("Invalid expression. It must contain '='.")
        return [], [], []

    lhs = tokens[0]
    rhs_tokens = tokens[2:]

    postfix = infix_to_postfix(rhs_tokens)

    stack = []
    for token in postfix:
        if token.isalnum():
            stack.append(token)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            temp = f"t{temp_count}"
            tac.append(f"{temp} = {op1} {token} {op2}")
            quads.append((token, op1, op2, temp))
            triples.append((token, op1, op2))
            stack.append(temp)
            temp_count += 1

    final = stack.pop()
    tac.append(f"{lhs} = {final}")
    quads.append(("=", final, "", lhs))
    triples.append(("=", final, ""))
    return tac, quads, triples

# 👉 User Input
user_expr = input("Enter an expression (e.g., a = (b + c) * (d - e)): ")

tac, quads, triples = generate_TAC_Quads_Triples(user_expr)

print("\n--- Three Address Code ---")
for line in tac:
    print(line)

print("\n--- Quadruples ---")
print("Op\tArg1\tArg2\tResult")
for q in quads:
    print(f"{q[0]}\t{q[1]}\t{q[2]}\t{q[3]}")

print("\n--- Triples ---")
print("Index\tOp\tArg1\tArg2")
for i, t in enumerate(triples):
    print(f"{i}\t{t[0]}\t{t[1]}\t{t[2]}")

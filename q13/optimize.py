import re

def parse_tac_line(line):
    """
    Parses a TAC line like: t1 = a + b
    Returns: (lhs, op1, operator, op2)
    """
    match = re.match(r'(\w+)\s*=\s*(\w+)\s*([\+\-\*/])\s*(\w+)', line)
    if match:
        return match.groups()
    
    # Constant assignment or direct copy
    match = re.match(r'(\w+)\s*=\s*(\w+)', line)
    if match:
        return match.group(1), match.group(2), None, None

    return None, None, None, None

def optimize_tac(tac_lines):
    optimized = []
    expr_map = {}
    value_map = {}
    used_vars = set()

    for line in tac_lines:
        lhs, op1, operator, op2 = parse_tac_line(line)

        if operator:  # it's a binary expression
            key = (op1, operator, op2)
            rev_key = (op2, operator, op1) if operator in ['+', '*'] else None

            if key in expr_map or (rev_key and rev_key in expr_map):
                reused = expr_map.get(key) or expr_map.get(rev_key)
                optimized.append(f"{lhs} = {reused}  # common subexpression")
            elif op1.isdigit() and op2.isdigit():
                result = str(eval(f"{op1}{operator}{op2}"))
                optimized.append(f"{lhs} = {result}  # constant folded")
                value_map[lhs] = result
            else:
                optimized.append(line)
                expr_map[key] = lhs
        else:  # assignment or copy
            if op1 in value_map:
                optimized.append(f"{lhs} = {value_map[op1]}  # copy propagation")
                value_map[lhs] = value_map[op1]
            else:
                optimized.append(line)
                value_map[lhs] = value_map.get(op1, op1)

        used_vars.add(lhs)

    # Dead Code Elimination (only removes if variable never used again)
    final_output = []
    seen_vars = set()
    for line in reversed(optimized):
        lhs = line.split('=')[0].strip()
        if lhs in seen_vars or any(op in seen_vars for op in line.split()[2:]):
            final_output.insert(0, line)
        else:
            seen_vars.add(lhs)
            final_output.insert(0, line)  # Keep all for now (can enhance dead code logic)

    return final_output

# ----------------------
# 🔧 Example usage:
# ----------------------
if __name__ == "__main__":
    print("Enter Three Address Code lines (type 'END' to finish input):")
    tac = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        tac.append(line.strip())

    print("\n🔍 Optimized Three Address Code:")
    optimized = optimize_tac(tac)
    for line in optimized:
        print(line)

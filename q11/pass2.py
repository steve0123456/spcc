# Two-Pass Assembler in Python (Pass 1 + Pass 2)

# Function to classify instruction type
def get_instruction_type(mnemonic):
    if mnemonic in ['START', 'END']:
        return 'AD'
    elif mnemonic in ['DS', 'DC']:
        return 'DL'
    elif mnemonic in ['READ', 'PRINT', 'MOVER', 'MOVEM', 'ADD', 'SUB', 'MUL', 'DIV']:
        return 'IS'
    return '??'

# Register codes
def get_register_code(register):
    registers = {
        'AREG': '01',
        'BREG': '02',
        'CREG': '03',
        'DREG': '04'
    }
    return registers.get(register, '00')

# Opcodes for instructions
def get_opcode(mnemonic):
    opcodes = {
        'STOP': '00',
        'ADD': '01',
        'SUB': '02',
        'MULT': '03',
        'MOVER': '04',
        'MOVEM': '05',
        'COMP': '06',
        'BC': '07',
        'DIV': '08',
        'READ': '09',
        'PRINT': '10'
    }
    return opcodes.get(mnemonic, '??')

# ----------------------- PASS 1 ------------------------
def pass1_assembler(lines):
    lc = 0
    symbol_table = {}
    sym_index = 0
    intermediate = []

    for line in lines:
        if not line.strip():
            continue

        tokens = line.strip().split()
        label = None

        # If line starts with a symbol
        if get_instruction_type(tokens[0]) == '??' and len(tokens) > 1:
            label = tokens[0]
            tokens = tokens[1:]
            if label not in symbol_table:
                symbol_table[label] = {'address': lc, 'index': sym_index}
                sym_index += 1

        mnemonic = tokens[0]
        inst_type = get_instruction_type(mnemonic)

        # START directive
        if mnemonic == "START":
            lc = int(tokens[1])
            intermediate.append(f"{lc} (AD,01) (C,{tokens[1]})")
            continue

        # END directive
        if mnemonic == "END":
            intermediate.append(f"{lc} (AD,02)")
            break

        # Declarative statements
        if mnemonic == "DS":
            intermediate.append(f"{lc} (S,{symbol_table[label]['index']}) (DL,0) (C,{tokens[1]})")
            lc += int(tokens[1])
            continue
        elif mnemonic == "DC":
            intermediate.append(f"{lc} (S,{symbol_table[label]['index']}) (DL,1) (C,{tokens[1]})")
            lc += 1
            continue

        # Imperative statements
        elif inst_type == "IS":
            if mnemonic in ['READ', 'PRINT']:
                operand = tokens[1]
                if operand not in symbol_table:
                    symbol_table[operand] = {'address': lc, 'index': sym_index}
                    sym_index += 1
                intermediate.append(f"{lc} (IS,{get_opcode(mnemonic)}) (S,{symbol_table[operand]['index']})")
            else:
                reg = tokens[1].replace(',', '')
                operand = tokens[2]
                if operand not in symbol_table:
                    symbol_table[operand] = {'address': lc, 'index': sym_index}
                    sym_index += 1
                intermediate.append(f"{lc} (IS,{get_opcode(mnemonic)}) (RG,{get_register_code(reg)}) (S,{symbol_table[operand]['index']})")
            lc += 1

    return symbol_table, intermediate

# ----------------------- PASS 2 ------------------------
def resolve_symbol(symbol_table, index):
    for sym in symbol_table.values():
        if sym['index'] == int(index):
            return sym['address']
    return 0

def pass2_assembler(symbol_table, intermediate_code):
    machine_code = []
    for line in intermediate_code:
        parts = line.split()
        lc = parts[0].rstrip(':')
        output = [lc]

        for token in parts[1:]:
            if token.startswith("(IS,"):
                opcode = token[4:-1]
                output.append(opcode)
            elif token.startswith("(RG,"):
                reg = token[4:-1]
                output.append(reg)
            elif token.startswith("(S,"):
                sym_index = token[3:-1]
                address = resolve_symbol(symbol_table, sym_index)
                output.append(str(address))
            elif token.startswith("(C,"):
                const = token[3:-1]
                output.append(const)
        if len(output) > 1:
            machine_code.append(" ".join(output))

    return machine_code

# ----------------------- MAIN ------------------------
if __name__ == "__main__":
    print("Enter assembly code (type END to finish):")
    lines = []
    while True:
        line = input()
        lines.append(line)
        if "END" in line:
            break

    # Run both passes
    symbol_table, intermediate_code = pass1_assembler(lines)
    machine_code = pass2_assembler(symbol_table, intermediate_code)

    print("\n=== SYMBOL TABLE ===")
    print("Symbol\tAddress\tIndex")
    for sym, info in symbol_table.items():
        print(f"{sym}\t{info['address']}\t{info['index']}")

    print("\n=== INTERMEDIATE CODE (PASS 1) ===")
    for line in intermediate_code:
        print(line)

    print("\n=== MACHINE CODE (PASS 2) ===")
    for line in machine_code:
        print(line)

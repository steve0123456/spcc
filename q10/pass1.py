def get_instruction_type(mnemonic):
    if mnemonic in ['START', 'END']:
        return 'AD'
    elif mnemonic in ['DS', 'DC']:
        return 'DL'
    elif mnemonic in ['READ', 'PRINT', 'MOVER', 'MOVEM', 'ADD', 'SUB', 'MUL', 'DIV']:
        return 'IS'
    return '??'

def get_register_code(register):
    registers = {
        'AREG': '01',
        'BREG': '02',
        'CREG': '03',
        'DREG': '04'
    }
    return registers.get(register, '00')

def pass1_assembler_user_input():
    print("Enter assembly code (type 'END' to finish):")
    lines = []
    while True:
        line = input()
        lines.append(line.strip())
        if line.strip().startswith("END"):
            break

    lc = 0
    symbol_table = {}
    sym_index = 0
    intermediate = []

    for line in lines:
        if not line:
            continue

        tokens = line.split()
        label = None
        if get_instruction_type(tokens[0]) == '??' and len(tokens) > 1:
            label = tokens[0]
            tokens = tokens[1:]
            if label not in symbol_table:
                symbol_table[label] = {'address': lc, 'index': sym_index}
                sym_index += 1

        mnemonic = tokens[0]
        inst_type = get_instruction_type(mnemonic)

        # START
        if mnemonic == "START":
            lc = int(tokens[1])
            intermediate.append(f"{lc} (AD,01) (C,{tokens[1]})")
            continue

        # END
        if mnemonic == "END":
            intermediate.append(f"{lc} (AD,02)")
            break

        # Data Declaration
        if mnemonic == "DS":
            intermediate.append(f"{lc} (S,{symbol_table[label]['index']}) (DL,0) (C,{tokens[1]})")
            lc += int(tokens[1])
            continue
        elif mnemonic == "DC":
            intermediate.append(f"{lc} (S,{symbol_table[label]['index']}) (DL,1) (C,{tokens[1]})")
            lc += 1
            continue

        # IS instructions
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

    # Output
    print("\n----- SYMBOL TABLE -----")
    for sym, val in symbol_table.items():
        print(f"{sym} -> {val['address']}")

    print("\n----- INTERMEDIATE CODE -----")
    for line in intermediate:
        print(line)

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


# Run the assembler
pass1_assembler_user_input()

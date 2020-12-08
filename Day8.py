import fileinput
import re
import copy


def parse():
    instructions = []

    for l in fileinput.input():
        instructions.append(l.strip().split(' '))

    return instructions


def execute(instructions):
    current_instr = 0
    acc = 0
    executed_instructions = set()

    while (current_instr not in executed_instructions) and (current_instr < len(instructions)):
        instr, val = instructions[current_instr]
        executed_instructions.add(current_instr)

        if instr == 'jmp':
            current_instr += int(val)

        elif instr == 'acc':
            acc += int(val)
            current_instr += 1

        elif instr == 'nop':
            current_instr += 1
        else:
            print('Unrecognized: ', instr)

    return current_instr >= len(instructions), acc


# Part 2
def fix_infinte_loop(instructions):
    for i, instruction in enumerate(instructions):
        if instruction[0] == 'jmp':
            instr = copy.deepcopy(instructions)
            instr[i][0] = 'nop'
            finite, acc = execute(instr)

            if finite:
                return acc

        if instruction[0] == 'nop':
            instr = copy.deepcopy(instructions)
            instr[i][0] = 'jmp'
            finite, acc = execute(instr)

            if finite:
                return acc


instructions = parse()

# Part 1
print(execute(instructions)[1])

# Part 2
print(fix_infinte_loop(instructions))

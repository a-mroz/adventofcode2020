import fileinput
import re

acc = 0

run_instructions = set()

instructions = []

for l in fileinput.input():
    instructions.append(l.strip().split(' '))


current_instr = 0

while current_instr not in run_instructions:
    instr, val = instructions[current_instr]
    run_instructions.add(current_instr)

    if instr == 'jmp':
        current_instr += int(val)

    if instr == 'acc':
        acc += int(val)
        current_instr += 1

    if instr == 'nop':
        current_instr += 1


print(acc)

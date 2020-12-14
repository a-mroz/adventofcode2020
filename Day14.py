import fileinput
import re
import copy


def parse():
    lines = [l.strip().split('=') for l in fileinput.input()]

    return [(instr, val) for instr, val in lines]


def task1(instr):
    mask = None
    mem = {}

    for i, v in instr:
        if i.startswith('mask'):
            mask = v.strip()
        elif i.startswith('mem'):
            addr = i[4:len(i)-2]
            val = list(str.zfill(bin(int(v))[2:], 36))

            for i, b in enumerate(mask):
                if b == 'X':
                    continue

                val[i] = b

            mem[addr] = int(''.join(val), 2)

        else:
            print(i)
            assert False

    return sum(mem.values())


def task2(instr):
    pass


# Part 1
instr = parse()
print(task1(instr))

# Part 2
print(task2(instr))

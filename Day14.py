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

    def all_addresses(acc, addr, mask, i):
        while i < len(mask) and mask[i] != 'X':
            i += 1

        if i >= len(mask):
            acc.append(int(''.join(addr), 2))
            return

        c1 = copy.deepcopy(addr)
        c1[i] = '0'

        c2 = copy.deepcopy(addr)
        c2[i] = '1'

        all_addresses(acc, c1, mask, i + 1)
        all_addresses(acc, c2, mask, i + 1)

    mask = None
    mem = {}

    for i, v in instr:
        if i.startswith('mask'):
            mask = v.strip()
        elif i.startswith('mem'):
            val = list(str.zfill(bin(int(i[4:len(i)-2]))[2:], 36))

            for i, m in enumerate(mask):
                if m == '0':
                    continue
                if m == '1':
                    val[i] = m

            addresses = []
            all_addresses(addresses, val, mask, 0)

            for addr in addresses:
                mem[addr] = int(v)
        else:
            print(i)
            assert False

    return sum(mem.values())


# Part 1
instr = parse()
print(task1(instr))

# Part 2
print(task2(instr))

import fileinput
import re
import copy


def parse():
    lines = [l.strip().split('=') for l in fileinput.input()]

    return [(instr, val) for instr, val in lines]


def task1(instruction):

    mask = None
    mem = {}

    # mem[xxx] = YYY
    mem_regex = re.compile(r'mem\[(\d+)\]')

    for instr, val in instruction:
        if instr.startswith('mask'):
            mask = val.strip()
        elif instr.startswith('mem'):
            addr = mem_regex.search(instr).group(1)

            val = list(str.zfill(bin(int(val))[2:], 36))

            for instr, b in enumerate(mask):
                if b == 'X':
                    continue

                val[instr] = b

            mem[addr] = int(''.join(val), base=2)

        else:
            print(instr)
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
            binary_str = list(str.zfill(bin(int(i[4:len(i)-2]))[2:], 36))

            for i, m in enumerate(mask):
                if m == '0':
                    continue
                if m == '1':
                    binary_str[i] = m

            addresses = []
            all_addresses(addresses, binary_str, mask, 0)

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

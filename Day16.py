import fileinput
import re
import copy


def parse():
    return [l.strip() for l in fileinput.input()]


def task1(lines):

    def parse_to_ranges_dict():
        ranges = {}
        for i, line in enumerate(lines[:20]):
            key = line.split(':')[0]
            a, b, c, d = re.findall(r'\d+', line)
            ranges[key] = [range(int(a), int(b) + 1),
                           range(int(c), int(d) + 1)]
        return ranges

    ranges = parse_to_ranges_dict()
    res = 0
    valid_tickets = []
    for i, line in enumerate(lines[25:]):
        count_valid_positions = 0

        numbers = [int(n) for n in line.split(',')]

        for n in numbers:
            valid = False

            for r in ranges.values():
                if n in r[0] or n in r[1]:
                    valid = True
                    continue

            if not valid:
                res += int(n)
            else:
                count_valid_positions += 1

        if count_valid_positions == len(line.split(',')):
            valid_tickets.append(numbers)

    return res, valid_tickets, ranges


def task2(valid_tickets, ranges):
    my_ticket = [73, 59, 83, 127, 137, 151, 71, 139, 67,
                 53, 89, 79, 61, 109, 131, 103, 149, 97, 107, 101]

    def get_initial_candidate_positions():
        candidate = set()
        for pos, n in enumerate(my_ticket):
            if n in rs[0] or n in rs[1]:
                candidate.add(pos)
        return candidate

    def remove_duplicates(candidates):
        sorted_candidates = {k: v for k, v in sorted(
            candidates.items(), key=lambda item: len(item[1]))}

        for k, n in sorted_candidates.items():
            for k1, n1 in sorted_candidates.items():
                if k != k1:
                    sorted_candidates[k1] = n1 - n
        return sorted_candidates

    candidates = {}
    for k, rs in ranges.items():
        candidate = get_initial_candidate_positions()

        for ticket in valid_tickets:
            for pos, n in enumerate(ticket):
                if not pos in candidate:
                    continue
                if not n in rs[0] and not n in rs[1]:
                    candidate.remove(pos)
        candidates[k] = copy.deepcopy(candidate)

    res = 1
    sorted_candidates = remove_duplicates(candidates)
    for k, v in sorted_candidates.items():
        if k.startswith('departure'):
            res *= my_ticket[v.pop()]

    return res


    # Part 1
lines = parse()
error_rate, valid_tickets, ranges = task1(lines)
print(error_rate)

# Part 2
print(task2(valid_tickets, ranges))

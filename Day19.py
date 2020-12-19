import fileinput
import re
import copy
import string


def parse():
    rules = {}
    messages = []

    for l in fileinput.input():
        if l.strip() == '':
            continue

        if not ':' in l:
            messages.append(l.strip())
        else:
            s = l.strip().split(':')
            rules[s[0]] = s[1].strip()

    return rules, messages


def task1(rules, messages):

    def recursive_regex(rule):
        res = ''

        if '|' in rule:
            res += '('

        for t in rule.split(' '):
            if t.isdigit():
                res += recursive_regex(rules[t])
            elif t == '|':
                res += t
            elif t == '"a"':
                res += 'a'
            elif t == '"b"':
                res += 'b'
            else:
                print('Unknown token', t)
                assert False

        if '|' in rule:
            res += ')'

        return res

    regex = '^' + recursive_regex(rules['0']) + '$'

    res = 0

    for m in messages:
        if re.match(regex, m):
            res += 1

    return res


def task2(rules, messages):
    res = 0
    return res


# Part 1
rules, messages = parse()
print(task1(rules, messages))

# Part 2
print(task2(rules, messages))

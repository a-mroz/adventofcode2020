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

        return res if '|' not in rule else '(' + res + ')'

        return res

    regex = '^' + recursive_regex(rules['0']) + '$'

    res = 0

    for m in messages:
        if re.match(regex, m):
            res += 1

    return res


def task2(rules, messages):

    def recursive_regex(rule_idx, in_loop_count=0):
        rule = rules[rule_idx]
        res = ''

        for t in rule.split(' '):
            if t.isdigit():
                loop = t == rule_idx
                if loop:
                    # Hacky. if we're looping for more than 5 times, just skip it
                    if (in_loop_count > 5):
                        continue

                    res += recursive_regex(t, in_loop_count + 1)
                else:
                    res += recursive_regex(t)
            elif t == '|':
                res += t
            elif t == '"a"':
                res += 'a'
            elif t == '"b"':
                res += 'b'
            else:
                print('Unknown token', t)
                assert False

        return res if '|' not in rule else '(' + res + ')'

    regex = '^' + recursive_regex('0') + '$'

    res = 0

    for m in messages:
        if re.match(regex, m):
            res += 1

    return res


# Part 1
rules, messages = parse()
print(task1(rules, messages))

# Part 2
rules_with_loop = copy.deepcopy(rules)
rules_with_loop['8'] = '42 | 42 8'
rules_with_loop['11'] = '42 31 | 42 11 31'
print(task2(rules_with_loop, messages))

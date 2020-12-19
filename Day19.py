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


def recursive_regex(rules, rule_idx, in_loop_count=0):
    rule = rules[rule_idx]
    res = ''
    
    for t in rule.split(' '):
        if t.isdigit():
            loop = t == rule_idx
            if loop:
                # Hacky. if we're looping for more than 5 times, just skip it
                if (in_loop_count > 5):
                    continue
                res += recursive_regex(rules, t, in_loop_count + 1)
            else:
                res += recursive_regex(rules, t)
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


def count_matching(rules, messages):
    regex = re.compile(recursive_regex(rules, '0'))

    return sum([1 if regex.fullmatch(message) else 0 for message in messages])


# Part 1
rules, messages = parse()
print(count_matching(rules, messages))

# Part 2
rules_with_loop = copy.deepcopy(rules)
rules_with_loop['8'] = '42 | 42 8'
rules_with_loop['11'] = '42 31 | 42 11 31'
print(count_matching(rules_with_loop, messages))

import fileinput
import re
import copy
import string


def parse():
    return [list(l.strip()) for l in fileinput.input()]


def to_postfix(line, precedence):
    res = []
    stack = []

    for c in line:
        if c == ' ':
            continue

        if c.isdigit():
            res.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack[-1] != '(':
                res.append(stack.pop())
            op = stack.pop()
        else:
            while len(stack) > 0 and (precedence[stack[-1]] >= precedence[c]):
                res.append(stack.pop())
            stack.append(c)

    while len(stack) > 0:
        res.append(stack.pop())

    return ' '.join(res)


def evaluate_postfix(l):
    stack = []

    for c in l:
        if c == ' ':
            continue

        if c.isdigit():
            stack.append(int(c))
        else:
            a = stack.pop()
            b = stack.pop()

            if c == '+':
                stack.append(a + b)
            elif c == '*':
                stack.append(a * b)
    return stack.pop()


def task1(lines):
    s = 0
    precedence = {'(': 1, '*': 2, '+': 2}  # equal precedence for + and *

    for l in lines:
        s += evaluate_postfix(to_postfix(l, precedence))
    return s


def task2(lines):
    s = 0
    precedence = {'(': 1, '*': 2, '+': 3}  # + has higher priority than *
    for l in lines:
        s += evaluate_postfix(to_postfix(l, precedence))
    return s


# Part 1
lines = parse()
print(task1(lines))

# Part 2
print(task2(lines))

import fileinput
from collections import deque, defaultdict
from itertools import islice, chain

card_pub = 1526110
door_pub = 20175123
divider = 20201227


def calculate_key(subject_number, loop_size):
    pub = 1
    for i in range(loop_size):
        pub *= subject_number
        pub %= divider
    return pub


def find_loop_size(pub_key):
    loop_size = 0
    subject_number = 7

    value = 1

    while value != pub_key:
        value *= subject_number
        value %= divider
        loop_size += 1

    return loop_size


def task1():
    loop_size_card = find_loop_size(card_pub)
    loop_size_door = find_loop_size(door_pub)

    encryption_key = calculate_key(card_pub, loop_size_door)

    assert encryption_key == calculate_key(door_pub, loop_size_card)

    return encryption_key


def task2():
    pass


# Part 1
print(task1())


# Part 2
print(task2())

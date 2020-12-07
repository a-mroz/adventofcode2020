import fileinput
import re

# A LOT of help from Redit today. A tough one.


def can_contain_shiny_gold(bag, policies):
    if bag not in policies or not policies[bag]:
        return False

    childs = policies[bag]

    if 'shiny gold' in childs:
        return True

    return any([can_contain_shiny_gold(child, policies) for child in childs])


def parse_policies():
    bags = set()
    policies = {}

    for l in fileinput.input():
        line = l.strip()
        parent = line.split('bags')[0].strip()
        childs = re.findall(
            r'\d+ ([a-z ]+) bag[s,.]*', line.split('contain')[1])

        policies[parent] = childs

        bags.add(parent)
    return bags, policies


bags, policies = parse_policies()
print(sum([can_contain_shiny_gold(bag, policies) for bag in bags]))

import fileinput
import re

# A LOT of help from Redit today. A tough one.


def can_contain_shiny_gold(bag, policies):
    if bag not in policies or not policies[bag]:
        return False

    childs = [color for (_, color) in policies[bag]]

    if 'shiny gold' in childs:
        return True

    return any([can_contain_shiny_gold(child, policies) for child in childs])


def child_bags(bags, policies):
    if not bags:
        return 0

    current_bag = bags[0]

    return int(current_bag[0]) * (1 + child_bags(policies[current_bag[1]], policies)) + child_bags(bags[1:], policies)


def parse_policies():
    bags = set()
    policies = {}

    for l in fileinput.input():
        line = l.strip()
        parent = line.split('bags')[0].strip()
        childs = re.findall(
            r'(\d+) ([a-z ]+) bag[s,.]*', line.split('contain')[1])

        policies[parent] = childs

        bags.add(parent)
    return bags, policies


bags, policies = parse_policies()
print(sum([can_contain_shiny_gold(bag, policies) for bag in bags]))
print(child_bags(policies['shiny gold'], policies))

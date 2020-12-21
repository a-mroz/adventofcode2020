import fileinput
import re
import copy
import string
from collections import Counter


def parse():
    food_with_alergens = []
    all_allergens = set()
    all_ingredients = set()

    for l in fileinput.input():

        s1 = l.strip().split('(')
        ingredients = [f.strip() for f in s1[0].strip().split(' ')]

        allergens = [a.strip() for a in s1[1][:-1].split(',')]
        allergens[0] = allergens[0].split(' ')[1]

        all_allergens |= set(allergens)
        all_ingredients |= set(ingredients)

        food_with_alergens.append((set(ingredients), set(allergens)))

    return food_with_alergens, all_allergens, all_ingredients


def task1(food_with_alergens, allergens, ingredients):
    allergic_ingredients = {}

    for a in allergens:
        candidates = None

        for ingr, al in food_with_alergens:
            if a in al:
                if candidates is None:
                    candidates = set(ingr)
                else:
                    candidates = candidates.intersection(ingr)

        allergic_ingredients[a] = candidates

    allergic = set()
    for _, ingr in allergic_ingredients.items():
        for i in ingr:
            allergic.add(i)

    res = set()
    for f, _ in food_with_alergens:
        for f1 in f:
            if f1 not in allergic:
                res.add(f1)

    return res


def task2(tiles, allergens, ingredients, not_allergic_ingredients):
    mapping = {}
    known = set()

    # while len(mapping) < len(allergens):
    #     for i in ingredients:
    #         candidates =

    # [('dairy', set()), ('eggs', {'dglm'}), ('fish', set()), ('peanuts', {'rbpg', 'zhqjs'}), ('sesame', {
    #     'xvtrfz'}), ('shellfish', {'tgmzqjz'}), ('soy', {'mfqgx'}), ('wheat', {'rffqhl', 'cdqvp'})]

    res = 0
    return res


# Part 1
food_with_alergens, allergens, ingredients = parse()


not_allergic_ingredients = task1(food_with_alergens, allergens, ingredients)
print(len(not_allergic_ingredients))

# Part 2
print(task2(food_with_alergens, allergens, ingredients, not_allergic_ingredients))

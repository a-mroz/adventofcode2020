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

    non_alergic_ingredients = set(ingredients)
    for _, ingr in allergic_ingredients.items():
        non_alergic_ingredients -= ingr

    return non_alergic_ingredients


def task2(food_with_alergens, allergens, ingredients, not_allergic_ingredients):
    mapping = {}
    candidates = {}

    known = set()

    for allergen in allergens:
        c = set(ingredients)
        for i, a in food_with_alergens:
            if allergen in a:
                c &= i
            candidates[allergen] = c.difference(not_allergic_ingredients)

    while len(mapping) < len(allergens):
        for allergen in allergens:
            if allergen in mapping.keys():
                continue

            candidate = set(candidates[allergen])
            candidate = candidate.difference(known)
            candidates[allergen] = candidate

            if len(candidate) == 1:
                k = next(iter(candidate))
                mapping[allergen] = k

                known.add(k)

    return mapping


# Part 1
food_with_alergens, allergens, ingredients = parse()
not_allergic_ingredients = task1(food_with_alergens, allergens, ingredients)

non_allergic_occurences = 0
for (ingr, _) in food_with_alergens:
    for i in ingr:
        if i in not_allergic_ingredients:
            non_allergic_occurences += 1

print(non_allergic_occurences)


# Part 2
allergen_to_food = task2(food_with_alergens, allergens,
                         ingredients, not_allergic_ingredients)


print(sorted(allergen_to_food.items()))

print(','.join([v for _, v in sorted(allergen_to_food.items())]))

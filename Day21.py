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


def non_allergic_ingredients(food_with_alergens, all_allergens, all_ingredients):
    allergic_ingredients = {}

    for allergen in all_allergens:
        candidates = set(all_ingredients)

        for ingredients, allergens in food_with_alergens:
            if allergen in allergens:
                candidates &= ingredients

        allergic_ingredients[allergen] = candidates

    non_alergic_ingredients = set(all_ingredients)
    for _, ingredients in allergic_ingredients.items():
        non_alergic_ingredients -= ingredients

    return non_alergic_ingredients


def task1(food_with_alergens, not_allergic):
    non_allergic_occurences = 0

    for ingredients, _ in food_with_alergens:
        for ingredient in ingredients:
            if ingredient in not_allergic:
                non_allergic_occurences += 1

    print(non_allergic_occurences)


def ingredients_by_allergy(food_with_allergens, all_allergens, all_ingredients, not_allergic_ingredients):
    candidates = {}

    for allergen in all_allergens:
        c = set(all_ingredients)
        for i, a in food_with_allergens:
            if allergen in a:
                c &= i
            candidates[allergen] = c.difference(not_allergic_ingredients)

    return candidates


def task2(food_with_alergens, all_allergens, all_ingredients, not_allergic_ingredients):
    mapping = {}
    candidates = ingredients_by_allergy(
        food_with_alergens, all_allergens, all_ingredients, not_allergic_ingredients)

    known = set()

    while len(mapping) < len(all_allergens):
        for allergen in all_allergens:
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

non_allergic_ingredients = non_allergic_ingredients(
    food_with_alergens, allergens, ingredients)

task1(food_with_alergens, non_allergic_ingredients)

# Part 2
allergen_to_food = task2(food_with_alergens, allergens,
                         ingredients, non_allergic_ingredients)

print(','.join([v for _, v in sorted(allergen_to_food.items())]))

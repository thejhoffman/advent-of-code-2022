import os

# Testing data ---------------------------------------------------------------
# /* cSpell:disable */
test = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]
# /* cSpell:enable */

# Setting up the data --------------------------------------------------------

# Read the input file
path = os.getcwd() + r"\puzzles\day3\input"
with open(path) as f:
    lines = f.read()

# Create a list of rucksacks
rucksacks = [line for line in lines.split("\n")]

# PART ONE -------------------------------------------------------------------


# helper function for splitting rucksacks into compartments
def compartmentalize(rucksack):
    middle = len(rucksack) // 2
    return [rucksack[:middle], rucksack[middle:]]


# function to find the shared item between two compartments in a rucksack
# this was refactored after getting the requirements from part 2
def find_shared_item_value(rucksack):
    lookup = {}
    length = len(rucksack)

    for index in range(length):
        for item in set(rucksack[index]):
            if item not in lookup:
                lookup[item] = 0
            lookup[item] += 1
            if lookup[item] == length:
                return get_priority(item)


# function to determine the priority of an item
def get_priority(item):
    if item.islower():
        return ord(item) - 96
    if item.isupper():
        return ord(item) - 38


# fmt: off
p1_solution = sum([
    find_shared_item_value(
        compartmentalize(item)
    )
    for item in rucksacks
])
# fmt: on

# Output for PART ONE
print("---PART ONE---")
print("Answer to puzzle:", p1_solution)

# PART TWO -------------------------------------------------------------------


# helper function to group up rucksacks in groups of 3
# found via: https://stackoverflow.com/a/434328
def chunk_list(seq, size):
    return (seq[pos : pos + size] for pos in range(0, len(seq), size))


# fmt: off
p2_solution = sum([
    find_shared_item_value(group)
    for group in chunk_list(rucksacks, 3)
])
# fmt: on

# Output for PART TWO
print("---PART TWO---")
print("Answer to puzzle:", p2_solution)

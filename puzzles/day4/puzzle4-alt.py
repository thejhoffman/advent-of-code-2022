import os

# Testing data ---------------------------------------------------------------
test = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8",
]

# Setting up the data --------------------------------------------------------

# Read the input file
path = os.getcwd() + r"\puzzles\day4\input"
with open(path) as f:
    lines = f.read()

# get data into workable format
assignments = [line for line in lines.split("\n")]

# group assignment pairs
test = [item.split(",") for item in test]
assignments = [item.split(",") for item in assignments]


# helper to covert assignment pairs into list of sections IDs
def convert_assignment_pairs(pair):
    first = pair[0].split("-")
    second = pair[1].split("-")

    first = [id for id in range(int(first[0]), int(first[1]) + 1)]
    second = [id for id in range(int(second[0]), int(second[1]) + 1)]

    return [first, second]


# final form of data, each assignment is a list of section ids in pairs
test = [convert_assignment_pairs(pair) for pair in test]
assignments = [convert_assignment_pairs(pair) for pair in assignments]

# PART ONE -------------------------------------------------------------------


# returns true if an assignment is fully contained in the other
def determine_if_fully_contains(pair):
    short = pair[0]
    long = pair[1]
    if len(pair[0]) > len(pair[1]):
        short = pair[1]
        long = pair[0]

    return set(short).issubset(set(long))


# fmt: off
p1_solution = [
    determine_if_fully_contains(pair)
    for pair in assignments
].count(True)
# fmt: on

# Output for PART ONE
print("---PART ONE---")
print("Answer to puzzle:", p1_solution)

# PART TWO -------------------------------------------------------------------


# returns true if an assignment has any overlap
def determine_if_any_overlap(pair):
    return bool(set(pair[0]).intersection(set(pair[1])))


# fmt: off
p2_solution = [
    determine_if_any_overlap(pair)
    for pair in assignments
].count(True)
# fmt: on

# Output for PART TWO
print("---PART TWO---")
print("Answer to puzzle:", p2_solution)

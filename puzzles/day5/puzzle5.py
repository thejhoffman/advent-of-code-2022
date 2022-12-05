import os
import re
import copy

# Testing data ---------------------------------------------------------------
test = """\
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

# Setting up the data --------------------------------------------------------

# Read the input file
path = os.getcwd() + r"\puzzles\day5\input.txt"
with open(path) as f:
    lines = f.read()


# helper function to process raws stack in usable data type
def process_initial_stacks(raw, length):
    raw = raw.split("\n")
    raw = [" " + stack for stack in raw]
    raw = [stack.replace("    ", " [ ]") for stack in raw]
    raw = [re.findall(r"\[(.*?)\]", stack) for stack in raw]
    raw.pop()

    stacks = []
    for _ in range(length):
        stacks.append([])

    for stack in raw[::-1]:
        for index, crate in enumerate(stack):
            if crate != " ":
                stacks[index].append(crate)
    return stacks


# function for processing data and extracting into workable data types
def process_data(data):
    # use regex to get just the stacks at beginning of input
    raw_stacks = re.findall("^[^1]*", data)[0]
    # remove the raw creates from rest of input data
    data = data.replace(raw_stacks, "")
    # get the length of the total number stacks, also using regex
    stack_length = int(re.findall("^([^\n]+)", data)[0].replace(" ", "")[-1])
    # get the final form of stacks
    stacks = process_initial_stacks(raw_stacks, stack_length)

    # remove the now unneeded stack numbers to just get the steps
    steps = data.split("\n\n")[1]
    # get the final form of the steps
    steps = [step for step in steps.split("\n")]

    return stacks, steps


t_stacks, t_steps = process_data(test)
stacks, steps = process_data(lines)

# PART ONE -------------------------------------------------------------------


# process steps for part one logic
def eval_steps(unmoved_stacks, steps):
    stacks = copy.deepcopy(unmoved_stacks)
    for step in steps:
        # fmt: off
        amount, source, destination = [
            int(item) for item in step.split(" ")
            if item.isnumeric()
        ]
        # fmt: on
        source -= 1
        destination -= 1
        for _ in range(amount):
            if stacks[source]:
                stacks[destination].append(stacks[source].pop())
    return stacks


p1_solution = "".join([stack[-1] for stack in eval_steps(stacks, steps)])

# Output for PART ONE
print("---PART ONE---")
print("Answer to puzzle:", p1_solution)

# PART TWO -------------------------------------------------------------------


# process steps for part two logic
def eval_steps_p2(unmoved_stacks, steps):
    stacks = copy.deepcopy(unmoved_stacks)
    for step in steps:
        # fmt: off
        amount, source, destination = [
            int(item) for item in step.split(" ")
            if item.isnumeric()
        ]
        # fmt: on
        source -= 1
        destination -= 1

        hold = []
        for _ in range(amount):
            if stacks[source]:
                hold.append(stacks[source].pop())
        [stacks[destination].append(crate) for crate in hold[::-1]]
    return stacks


p2_solution = "".join([stack[-1] for stack in eval_steps_p2(stacks, steps)])

# Output for PART TWO
print("---PART TWO---")
print("Answer to puzzle:", p2_solution)

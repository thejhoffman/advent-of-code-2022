import os
import heapq

# Setting up the data --------------------------------------------------------

# Read the input file
path = os.getcwd() + r"\puzzles\day1\input"
with open(path) as f:
    lines = f.readlines()

# Create a list of elves with their food from the input
elves = []
create_elf = []
for line in lines:
    line = line.rstrip()
    if line:
        create_elf.append(eval(line))
    else:
        elves.append(create_elf)
        create_elf = []

# Combine food into calorie totals
elf_totals = [sum(elf) for elf in elves]

# PART ONE -------------------------------------------------------------------


# Method 1 - Find the elf with most calories
most_calories = 0
for elf in elf_totals:
    if elf > most_calories:
        most_calories = elf

# Alternate Method 2
alternate = max(elf_totals)

# Output for PART ONE
print("---PART ONE---")
print("Answer to puzzle method 1:", most_calories)
print("Alternate method 2 answer:", alternate)

# PART TWO -------------------------------------------------------------------


# Method 1 - Find top three elves with most calories
first, second, third = -1, -1, -1
for elf in elf_totals:
    if elf > first:
        first, second, third = elf, first, second
    elif first > elf > second:
        second, third = elf, second
    elif second > elf > third:
        third = elf

solution1 = sum([first, second, third])

# Alternate Method 2
alt2_list = elf_totals
alt2 = sum(heapq.nlargest(3, alt2_list))

# Alternate Method 3
# Note: destructive to original list unless a copy is used
# In this case a shallow copy is fine
alt3_list = [*elf_totals]
alt3 = sum(
    [
        alt3_list.pop(alt3_list.index(max(alt3_list))),
        alt3_list.pop(alt3_list.index(max(alt3_list))),
        alt3_list.pop(alt3_list.index(max(alt3_list))),
    ]
)

# Alternate Method 4
alt4_list = sorted(elf_totals)
alt4 = sum(
    [
        alt4_list[-1],
        alt4_list[-2],
        alt4_list[-3],
    ]
)

# Output for PART 2
print("---PART TWO---")
print("Answer to puzzle method 1:", solution1)
print("Alternate method 2 answer:", alt2)
print("Alternate method 3 answer:", alt3)
print("Alternate method 4 answer:", alt4)

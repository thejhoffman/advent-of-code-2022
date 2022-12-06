import os

# Testing data ---------------------------------------------------------------
# /* cSpell:disable */
test1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
test2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
test3 = "nppdvjthqldpwncqszvftbrmjlhg"
test4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
test5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
# /* cSpell:enable */

# Setting up the data --------------------------------------------------------

# Read the input file
path = os.getcwd() + r"\puzzles\day6\input"
with open(path) as f:
    lines = f.read()

datastream = lines

# PART ONE -------------------------------------------------------------------


def find_start(stream, length=4):
    for index in range(len(stream[length - 1 :])):
        start = index
        end = index + length
        marker = stream[start:end]
        if len(marker) == len(set(marker)):
            return index + length


p1_solution = find_start(datastream)

# Output for PART ONE
print("---PART ONE---")
print("Answer to puzzle:", p1_solution)

# PART TWO -------------------------------------------------------------------

p2_solution = find_start(datastream, length=14)

# Output for PART TWO
print("---PART TWO---")
print("Answer to puzzle:", p2_solution)

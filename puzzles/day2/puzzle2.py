import os

# Setting up the data --------------------------------------------------------

# Read the input file
path = os.getcwd() + r"\puzzles\day2\input"
with open(path) as f:
    lines = f.read()

# Create a list of the RPS combinations suggested by guide
guide = [line.split(" ") for line in lines.split("\n")]


# PART ONE -------------------------------------------------------------------

# define function to evaluate result of a combination
def eval_combo(combo):
    opponent_keys = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
    }

    my_keys = {
        "X": ["rock", 1],
        "Y": ["paper", 2],
        "Z": ["scissors", 3],
    }

    opponent = opponent_keys[combo[0]]
    me, shape_points = my_keys[combo[1]][0], my_keys[combo[1]][1]

    if opponent == me:
        return 3 + shape_points

    match opponent:
        case "rock":
            if me == "paper":
                return 6 + shape_points
            return 0 + shape_points
        case "paper":
            if me == "scissors":
                return 6 + shape_points
            return 0 + shape_points
        case "scissors":
            if me == "rock":
                return 6 + shape_points
            return 0 + shape_points


p1_solution = sum([eval_combo(combo) for combo in guide])

# Output for PART ONE
print("---PART ONE---")
print("Answer to puzzle:", p1_solution)


# PART TWO -------------------------------------------------------------------

# define function to evaluate result of a combination, altered
def eval_combo_p2(combo):
    shape_keys = {
        "A": ["rock", 1],
        "B": ["paper", 2],
        "C": ["scissors", 3],
    }

    outcome_keys = {
        "X": "lose",
        "Y": "draw",
        "Z": "win",
    }

    opponent = shape_keys[combo[0]][0]
    choice = outcome_keys[combo[1]]

    match choice:
        case "lose":
            match opponent:
                case "rock":  # pick scissors to lose
                    shape_points = shape_keys["C"][1]
                case "paper":  # pick rock to lose
                    shape_points = shape_keys["A"][1]
                case "scissors":  # pick paper to lose
                    shape_points = shape_keys["B"][1]
            return 0 + shape_points
        case "draw":  # pick same as opponent to draw
            return 3 + shape_keys[combo[0]][1]
        case "win":
            match opponent:
                case "rock":  # pick scissors to win
                    shape_points = shape_keys["B"][1]
                case "paper":  # pick rock to win
                    shape_points = shape_keys["C"][1]
                case "scissors":  # pick paper to win
                    shape_points = shape_keys["A"][1]
            return 6 + shape_points


p2_solution = sum([eval_combo_p2(combo) for combo in guide])

# Output for PART TWO
print("---PART TWO---")
print("Answer to puzzle:", p2_solution)

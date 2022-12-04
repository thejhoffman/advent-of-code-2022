import os

# Setting up the data --------------------------------------------------------

# Read the input file
path = os.getcwd() + r"\puzzles\day2\input"
with open(path) as f:
    lines = f.read()

# Create a list of the RPS combinations suggested by guide
guide = [line.split(" ") for line in lines.split("\n")]

# PART ONE -------------------------------------------------------------------


# function to get the shape based off the input
def get_shape(str):
    shape_lookup = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }
    return shape_lookup.get(str)


# function to get a value base off the shape
def get_shape_value(shape):
    match shape:
        case "rock":
            return 1
        case "paper":
            return 2
        case "scissors":
            return 3


# function to get the score of round given a combo of inputs
def score_round(combo):
    opponent_shape = get_shape(combo[0])
    my_shape = get_shape(combo[1])

    my_shape_value = get_shape_value(my_shape)

    # check for winner
    match [opponent_shape, my_shape]:
        case ["rock", "paper"]:
            return 6 + my_shape_value
        case ["paper", "scissors"]:
            return 6 + my_shape_value
        case ["scissors", "rock"]:
            return 6 + my_shape_value

    # check for draw
    if opponent_shape == my_shape:
        return 3 + my_shape_value

    # loss if other checks failed
    return 0 + my_shape_value


p1_solution = sum([score_round(combo) for combo in guide])

# Output for PART ONE
print("---PART ONE---")
print("Answer to puzzle:", p1_solution)

# PART TWO -------------------------------------------------------------------


# function to get outcome based off the input
def get_outcome(str):
    outcome_lookup = {
        "X": "lose",
        "Y": "draw",
        "Z": "win",
    }
    return outcome_lookup.get(str)


# function to get the my shape base off the opponents shape and outcome
def get_my_shape(opponent_shape, outcome):
    match outcome:
        case "lose":
            match opponent_shape:
                case "rock":  # pick scissors to lose
                    return "scissors"
                case "paper":  # pick rock to lose
                    return "rock"
                case "scissors":  # pick paper to lose
                    return "paper"
        case "draw":  # pick same as opponent to draw
            return opponent_shape
        case "win":
            match opponent_shape:
                case "rock":  # pick paper to win
                    return "paper"
                case "paper":  # pick scissors to win
                    return "scissors"
                case "scissors":  # pick rock to win
                    return "rock"


# function to get point base off the outcome
def get_points(outcome):
    match outcome:
        case "lose":
            return 0
        case "draw":
            return 3
        case "win":
            return 6


# function to get the score of round given a combo of inputs
def score_round_p2(combo):
    opponent_shape = get_shape(combo[0])
    outcome = get_outcome(combo[1])
    my_shape = get_my_shape(opponent_shape, outcome)
    my_shape_value = get_shape_value(my_shape)
    return get_points(outcome) + my_shape_value


p2_solution = sum([score_round_p2(combo) for combo in guide])

# Output for PART TWO
print("---PART TWO---")
print("Answer to puzzle:", p2_solution)

OP_MOVES = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS"
}

MY_MOVES = {
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSORS"
}

WIN_PAIR = {
    "ROCK": "PAPER",     # PAPER beats ROCK
    "PAPER": "SCISSORS", # SCISSORS beats PAPER
    "SCISSORS": "ROCK"   # ROCK beats SCISSORS 
}

MOVE_POINT = {
    "ROCK": 1,     # PAPER beats ROCK
    "PAPER": 2, # SCISSORS beats PAPER
    "SCISSORS": 3   # ROCK beats SCISSORS 
}

OUTCOME_POINT = {
    "win": 6,
    "draw": 3,
    "lose": 0
}

def is_draw(OP_MOVE, MY_MOVE):
    return OP_MOVES[OP_MOVE] == MY_MOVES[MY_MOVE]

def is_win(OP_MOVE, MY_MOVE):
    return WIN_PAIR[OP_MOVES[OP_MOVE]] == MY_MOVES[MY_MOVE]

def get_score(MY_MOVE, OUTCOME):
    return MOVE_POINT[MY_MOVES[MY_MOVE]] + OUTCOME_POINT[OUTCOME]

with open("input.txt", "r") as f:
    lines = f.readlines()

    running_score = 0
    for line in lines:
        l = line.strip()
        [OP, ME] = l.split(" ")

        outcome = ""
        if is_draw(OP, ME):
            outcome = "draw"
        elif is_win(OP, ME):
            outcome = "win"
        else:
            outcome = "lose"

        current_score = get_score(ME, outcome)
        running_score += current_score 

    print(running_score)

    
FIRST_COLS = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS"
}

SECOND_COLS = {
    "X": "LOSE",
    "Y": "DRAW",
    "Z": "WIN"
}

WIN_MATCH = {
    "ROCK": "PAPER",     # PAPER beats ROCK
    "PAPER": "SCISSORS", # SCISSORS beats PAPER
    "SCISSORS": "ROCK"   # ROCK beats SCISSORS 
}

LOSE_MATCH = {
    "ROCK": "SCISSORS",
    "PAPER": "ROCK",
    "SCISSORS": "PAPER"
}

DRAW_MATCH = {
    "ROCK": "ROCK",     
    "PAPER": "PAPER", 
    "SCISSORS": "SCISSORS"   
}

FINAL_MATCH_MAP = {
    "WIN": WIN_MATCH,
    "LOSE": LOSE_MATCH,
    "DRAW": DRAW_MATCH
}

OUTCOME_POINT = {
    "WIN": 6,
    "DRAW": 3,
    "LOSE": 0
}

MOVE_POINT = {
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3
}

def get_my_move(OP_MOVE, OUTCOME):
    OP_MOVE = FIRST_COLS[OP_MOVE]
    OUTCOME = SECOND_COLS[OUTCOME]

    out = FINAL_MATCH_MAP[OUTCOME][OP_MOVE]
    return out

def get_score(MY_MOVE, OUTCOME):
    return MOVE_POINT[MY_MOVE] + OUTCOME_POINT[SECOND_COLS[OUTCOME]]

with open("input.txt", "r") as f:
    lines = f.readlines()

    running_score = 0
    for line in lines:
        l = line.strip()
        [OP, OUTCOME] = l.split(" ")

        MY_MOVE = get_my_move(OP, OUTCOME)
        
        current_score = get_score(MY_MOVE, OUTCOME)
        running_score += current_score

    print(running_score)

    
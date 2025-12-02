# RPS.py

import random

def player(prev_play, opponent_history=[]):

    if prev_play != "":
        opponent_history.append(prev_play)

    if len(opponent_history) < 3:
        return random.choice(["R", "P", "S"])

    counter = {"R": "P", "P": "S", "S": "R"}

    # --- Strategy 1: Counter most common move ---
    most_common = max(set(opponent_history), key=opponent_history.count)
    move1 = counter[most_common]

    # --- Strategy 2: Pattern matching for smarter bots ---
    last3 = "".join(opponent_history[-3:])
    patterns = {}

    for i in range(len(opponent_history) - 3):
        key = "".join(opponent_history[i:i+3])
        next_move = opponent_history[i+3]

        if key not in patterns:
            patterns[key] = {"R": 0, "P": 0, "S": 0}
        patterns[key][next_move] += 1

    if last3 in patterns:
        predicted = max(patterns[last3], key=patterns[last3].get)
        move2 = counter[predicted]
    else:
        move2 = move1

    # Strategy switching
    if len(opponent_history) < 30:
        return move1
    else:
        return move2

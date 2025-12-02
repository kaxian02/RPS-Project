# RPS_game.py

import random

def beats(one, two):
    return ((one == "R" and two == "S") or
            (one == "S" and two == "P") or
            (one == "P" and two == "R"))

def play(player1, player2, num_games, verbose=False):
    p1_prev = ""
    p2_prev = ""
    p1_score = 0
    p2_score = 0

    for _ in range(num_games):
        p1_move = player1(p2_prev)
        p2_move = player2(p1_prev)

        if beats(p1_move, p2_move):
            p1_score += 1
        elif beats(p2_move, p1_move):
            p2_score += 1

        p1_prev = p1_move
        p2_prev = p2_move

        if verbose:
            print(f"P1: {p1_move} | P2: {p2_move}")

    return p1_score, p2_score


# Bots
def quincy(prev):
    choices = ["R", "P", "S", "R", "P"]
    return choices[random.randint(0, 4)]

def mrugesh(prev, history=[]):
    if prev != "":
        history.append(prev)
    if len(history) < 5:
        return random.choice(["R", "P", "S"])
    counts = {"R": history.count("R"),
              "P": history.count("P"),
              "S": history.count("S")}
    guess = max(counts, key=counts.get)
    return {"R": "P", "P": "S", "S": "R"}[guess]

def kris(prev, history=[]):
    if prev != "":
        history.append(prev)
    if len(history) < 3:
        return random.choice(["R", "P", "S"])
    return {"R": "P", "P": "S", "S": "R"}[history[-2]]

def abbey(prev, history=[]):
    if prev != "":
        history.append(prev)
    if len(history) < 4:
        return random.choice(["R", "P", "S"])
    last_two = history[-2:]
    if last_two == ["R", "R"]:
        return "P"
    elif last_two == ["P", "P"]:
        return "S"
    elif last_two == ["S", "S"]:
        return "R"
    return random.choice(["R", "P", "S"])

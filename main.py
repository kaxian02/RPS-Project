# main.py

from RPS_game import play, quincy, mrugesh, kris, abbey
from RPS import player

# Test your bot manually
print("Testing vs Quincy…")
print(play(player, quincy, 1000))

print("Testing vs Mrugesh…")
print(play(player, mrugesh, 1000))

print("Testing vs Kris…")
print(play(player, kris, 1000))

print("Testing vs Abbey…")
print(play(player, abbey, 1000))

# Uncomment to run FCC tests
# from test_module import test
# test(player)

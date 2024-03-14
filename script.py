from settings import *
from players import *
from game import *

print("====================================================")
print("WELCOME TO CONNECT FOUR!")
print("====================================================")


user_input = input("Choose mode (PVE / PVP): ")
if len(user_input) > 0:
    user_input = user_input.upper()
    if user_input == 'PVE':
        player = Player("X")
        computer = Computer()
        game = Game(player, computer)
        game.run()
    elif user_input == 'PVP':
        player_1 = Player("X")
        player_2 = Player("O")
        game = Game(player_1, player_2)
        game.run()
    else:
        print("Invalid input. Try again.")
else:
    print("You didn't choose any mode. Try Again.")
#"""    
    

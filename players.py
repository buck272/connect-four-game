from settings import *

class Player():
    def __init__(self, symbol):
        self.symbol = symbol
    def choose_column(self):
        player_input = input("Choose column (1-7): ")
        if len(player_input) > 0:
            player_input = int(player_input) - 1
            if player_input >= 0 and player_input <= 6:
                return player_input
            else:
                return "Invalid input. Try Again."
        else:
            return "You didn't choose any column. Try Again."
        
            
class Computer():
    def __init__(self):
        self.symbol = "O"
    def choose_column(self):
        computer_choice = random.randint(0, 6)
        return computer_choice
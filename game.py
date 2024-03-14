from settings import *

class Game():
    def __init__(self, player_one, player_two):
        self.p1 = player_one
        self.p2 = player_two
        
    def update_board(self, game_board, visual_board):
        for i in range(len(game_board)):
            if len(game_board[i]) > 0 and len(game_board[i]) <= 6:
                for j in range(len(game_board[i])):
                    visual_board[i][j] = game_board[i][j]
        return visual_board
    
    def show_board(self, board):
        print("=============================")
        print("| {} | {} | {} | {} | {} | {} | {} |".format(board[0][5],board[1][5],board[2][5],board[3][5],board[4][5],board[5][5],board[6][5]))
        print("=============================")
        print("| {} | {} | {} | {} | {} | {} | {} |".format(board[0][4],board[1][4],board[2][4],board[3][4],board[4][4],board[5][4],board[6][4]))
        print("=============================")
        print("| {} | {} | {} | {} | {} | {} | {} |".format(board[0][3],board[1][3],board[2][3],board[3][3],board[4][3],board[5][3],board[6][3]))
        print("=============================")
        print("| {} | {} | {} | {} | {} | {} | {} |".format(board[0][2],board[1][2],board[2][2],board[3][2],board[4][2],board[5][2],board[6][2]))
        print("=============================")
        print("| {} | {} | {} | {} | {} | {} | {} |".format(board[0][1],board[1][1],board[2][1],board[3][1],board[4][1],board[5][1],board[6][1]))
        print("=============================")
        print("| {} | {} | {} | {} | {} | {} | {} |".format(board[0][0],board[1][0],board[2][0],board[3][0],board[4][0],board[5][0],board[6][0]))
        print("=============================")
    
    def column_is_full(self, game_board, chosen_column):
        if len(game_board[chosen_column]) == 6:
            return True
        else:
            return False
    
    def has_winner(self, game_board):
        sample_1 = ["X","X","X","X"]
        sample_2 = ["O","O","O","O"]
        has_winner = False
        no_winner = True
        while no_winner:
            for col in game_board:
                if (col[0:4] or col[1:5] or col[2:]) == sample_1:
                    has_winner = True
                elif (col[0:4] or col[1:5] or col[2:]) == sample_2:
                    has_winner = True
            else:
                no_winner = False
        return has_winner
        
    def run(self):
        turn = 1
        running = True
        while running:
            self.update_board(game_board, visual_board)
            self.show_board(visual_board)
            if self.has_winner(game_board):
                if turn == 1:
                    print("The winner is player 2!")
                elif turn == -1:
                    print("The winner is player 1!")
                running = False
                break
                
            if turn == 1:
                pick_column = True
                while pick_column:
                    column = self.p1.choose_column()
                    if self.column_is_full(game_board, column):
                        print("Column full, choose another column.")
                        continue
                    else:
                        game_board[column].append(self.p1.symbol)
                        turn *= -1
                        pick_column = False
            elif turn == -1:
                pick_column = True
                while pick_column:
                    column = self.p2.choose_column()
                    if self.column_is_full(game_board, column):
                        print("Column full, choose another column.")
                        continue
                    else:
                        game_board[column].append(self.p2.symbol)
                        turn *= -1
                        pick_column = False
import math
import random
#the game has two players (comp-human,human-human,comp-comp)- one with X and another with O which they place on board. 
#they get alternate chances (switching)
#the board has 9 squares (only can place in non occupied square)- have to create -matrix (3X3)
#scenarios for win - vertical, horizontal and diagonal 
#scenario for draw - win not met- board sqaures are filled.

#players, board
#give_chance, check_win, check_draw, check_valid_move, reset(?)

#parent class
class Player:
    def __init__(self,letter):
        # letter is x or o
        self.letter = letter

    def get_move(self,game):
        #all players should get their move in the game
        pass

#child class
class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        square = random.choice(game.available_moves())
        return square

#child class
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self,game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\s turn. Input move [0-8]: ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val
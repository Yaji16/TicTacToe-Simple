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

#child class
class GeniusComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) #randomly choose one square
        else:
            #pick a square base of the minmax algorithm
            square = (self.minimax(self.letter,game))['position']
        return square
    
    def minimax(self,player,state):
        max_player = self.letter
        other_player = 'O' if max_player=='X' else 'X'

        #when do we stop finding other moves? when one of the player wins 
        # this will be our base case - as finding moves for each state is recursive in nature
        if state.current_winner == other_player:
            return {'position': None,
                    'score': 1*(state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)
                    }
        
        elif not state.empty_squares():
            return {'position':None, 'score': 0}

        if player == max_player: #maximize the score
            best = {'position': None, 'score': -math.inf}
        else: #minimize the score
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            #step 1: make a move, try that spot
            state.make_move(possible_move, player)
            #step 2: recurse using minmax to simulate a game after making that move
            sim_score = self.minimax(other_player,state) #we have to alternate the player
            #step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            #step 4: update the dictionaries if necessary
            if player == max_player: #maximize max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else: #minimize min player
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
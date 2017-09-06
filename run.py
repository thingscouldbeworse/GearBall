from random import randint
from ball import ball
from ball_components import face, piece, gear
import util
import sys

def randomize(num_moves):
    
    our_ball = ball()
    our_ball.output_ball()
    
    for i in range(0, num_moves):
        # we start with all possible moves,
        # but the randomizer will not produce
        # a sequence that involves an undone move 
        possible_moves = {
                'top': {
                    'right': ['center', 'bottom'],
                    'left': ['center', 'bottom']
                    },
                'bottom': {
                    'right': ['center', 'top'],
                    'left': ['center', 'top']
                    },
                'right': {
                    'up': ['center', 'left'],
                    'down': ['center', 'left']
                    },
                'left': {
                    'up': ['center', 'right'],
                    'down': ['center', 'right']
                    }
                }

        key_index = randint(0,3)
        row = (list(possible_moves.keys()))[key_index]
        possible_moves = possible_moves[row]
        direction = (list(possible_moves.keys()))[randint(0,1)]
        possible_moves = possible_moves[direction]
        hold = possible_moves[randint(0,1)]
        
        our_ball.move(row, direction, hold)
        our_ball.output_ball() 

randomize(20)   

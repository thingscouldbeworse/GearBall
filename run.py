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
        # a sequence that involves undoing a previous move 
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

        if i > 0:
            previous_hold = hold
            previous_direction = direction
            previous_row = row
            opposite_direction = util.get_opposite(direction)
        else:
            previous_hold = ''
            previous_row = ''

        done = False

        while not done:
            key_index = randint(0,3)
            row = (list(possible_moves.keys()))[key_index]
            possible_move_subset = possible_moves[row]
            direction = (list(possible_move_subset.keys()))[randint(0,1)]
            possible_move_subset = possible_move_subset[direction]
            hold = possible_move_subset[randint(0,1)]
            
            if row == previous_row and hold == previous_hold and direction == opposite_direction:
                done = False
            else:
                done = True
 
        our_ball.move(row, direction, hold)
        our_ball.output_ball() 

if len(sys.argv) < 2:
    print("Usage: 'python run.py [number of random moves to generate]")
else:
    randomize(int(sys.argv[1]))

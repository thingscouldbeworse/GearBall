from random import randint
from ball import ball
from ball_components import face, piece, gear
import util
import sys

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

def randomize(num_moves):
    
    our_ball = ball()
    our_ball.output_ball()
    
    for i in range(0, num_moves):
        # we start with all possible moves,
        # but the randomizer will not produce
        # a sequence that involves undoing a previous move 
        
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

def build_possible_state_branch(our_ball):
    
    # "state" is actually just the string representation of the ball
    # we hold on to the ball objects anyway so we can choose one
    possibe_states = []
    for row in possible_moves:
        for direction in row:
            for hold in direction:
                new_ball = ball()
                new_ball.move(row, direction, hold)
                new_ball.textify_rows()
                possible_states.append(new_ball)
    return possible_states 
    
def main():
    if len(sys.argv) < 2 or len(sys.argv) >= 6:
        print("Usage: ")
        print("         python run.py [number of random moves to generate]")
        print("         python run.py [row to move] [direction] [row to hold]")
        print("         python run,py [row to move] [direction] [row to hold] [quit after execute, don't wait for more input]")
    elif len(sys.argv) == 2:
        randomize(int(sys.argv[1]))
    elif len(sys.argv) > 2 and len(sys.argv) < 6:
        our_ball = ball()
        our_ball.output_ball()
        
        done = False
        row = sys.argv[1]
        direction = sys.argv[2]
        hold = sys.argv[3]

        while not done:
            our_ball.move(row, direction, hold)
            our_ball.output_ball()
            if len(sys.argv) > 4:
                done = True
            else:
                move = input("Next move: ")
                if move == 'quit' or move == 'q':
                    done = True
                else:
                    row, direction, hold = list(move.split(' '))

if __name__ == "__main__":
    main()


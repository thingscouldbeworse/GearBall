from random import randint
from ball import ball
from ball_components import face, piece, gear
import solve
import util
import sys
import copy

# 8 moves are equivalents of each other (top right center is 
# equivalent of bottom left center) so we can remove those options
possible_moves = {
                'top': {
                    'right': ['center', 'bottom'],
                    'left': ['center', 'bottom']
                    },
                'bottom': {
                    'right': ['top'],
                    'left': ['top']
                    },
                'right': {
                    'up': ['left'],
                    'down': ['left']
                    },
                'left': {
                    'up': ['center', 'right'],
                    'down': ['center', 'right']
                    }
                }
possible_rotations = [
                    'right',
                    'up',
                    'left',
                    'down'
                    ]

# randomize by building state branches and choosing a state. Slow.
def randomize_state(num_moves):
    
    our_ball = ball()
    our_ball.output_ball()
    previous_state = ""
    
    for i in range(0, num_moves):
        # we start with all possible moves, but the randomizer will not produce
        # a sequence that involves undoing a previous move, or a move that will
        # result in a 90 degree rotation of the ball (functionally undoing)

        possible_ball_states = build_possible_state_branch(our_ball)

        # if any of the possible moves generated would return us to the previous
        # state remove them from the pool of possible moves
        bad_move = -1
        for i in range(0, len(possible_ball_states)):
            if possible_ball_states[i].rows == previous_state:
                bad_move = i
        
        if bad_move != -1:
            del possible_ball_states[bad_move]

        chosen_move = randint(0, len(possible_ball_states)-1)
        previous_state = our_ball.rows
        our_ball = possible_ball_states[chosen_move]

        our_ball.output_ball() 

# simple move move check, much faster, does allow for complex avoidance.
# still needs performance improvements, especially for 90 and 180 turns 
def randomize_quick(num_moves, return_ball=False):
    
    our_ball = ball()
    our_ball.output_ball()
    previous_rotation_states = [""] * 6
    previous_state = ""
    
    for i in range(0, num_moves):
                
        done = False
        
        temp_ball = copy.deepcopy(our_ball)
        while not done:
            key_index = randint(0,len(possible_moves)-1)
            row = (list(possible_moves.keys()))[key_index]
            possible_move_subset = possible_moves[row]
            direction = (list(possible_move_subset.keys()))[randint(0,len(possible_move_subset)-1)]
            possible_move_subset = possible_move_subset[direction]
            hold = possible_move_subset[randint(0,len(possible_move_subset)-1)]
            output = temp_ball.move(row, direction, hold, verbose=False)

            temp_ball.textify_rows()

            if temp_ball.rows == previous_state:
                print("regenerating")
                done = False
            else:
                done = True

            for rotation_state in previous_rotation_states:
                if temp_ball.rows == rotation_state:
                    done = False
                    print("rotate")
                    break

        previous_state = our_ball.rows
        # stash the 6 possible rotation states to compare against
        for i in range(0,6):
            temp_ball_2 = copy.deepcopy(our_ball)
            if i < 4:
                temp_ball_2.rotate(possible_rotations[i])
            elif i > 3:
                temp_ball_2.rotate(possible_rotations[i-4])
                temp_ball_2.rotate(possible_rotations[i-4])
            previous_rotation_states[i] = temp_ball.rows

        our_ball = copy.deepcopy(temp_ball)
        print(output)
        our_ball.output_ball() 
    if return_ball:
        return our_ball

def build_possible_state_branch(our_ball, onlycenter=False):
    
    # "state" is actually just the string list representation of the ball
    possible_states = []
    temp_ball = ball()
    for row in possible_moves:
        for direction in possible_moves[row]:
            for hold in possible_moves[row][direction]:
                if hold == "center" and onlycenter:
                    temp_ball = copy.deepcopy(our_ball)
                    output = temp_ball.move(row, direction, hold, verbose=False)
                    possible_states.append(temp_ball)
                elif onlycenter == False:
                    temp_ball = copy.deepcopy(our_ball)
                    output = temp_ball.move(row, direction, hold, verbose=False)
                    possible_states.append(temp_ball)
    return possible_states 

def solve_ball(this_ball):
    
    closedSet = []
    openSet = []
    cameFrom = []
    depth = 1
    
    scores = []
    states = build_possible_state_branch(this_ball, True)
    for state in states:
        scores.append([state, 100000, 10000])
    openSet.append([this_ball, solve.hs(this_ball), 0])

    current = ['',100000, 0]
    while len(openSet) > 0:
        print("looping")
        for node in openSet:
            if node[1] < current[1]:
                current[0] = node[0]
                current[1] = node[1]
                current[2] = node[2]
            if current[1] < 47:
                print("found solution")
                return cameFrom

            closedSet.append(current)
            openSet.remove(node)

        states = build_possible_state_branch(current[0], True)
        current[0].output_ball()
        scores = []
        for state in states:
            scores.append([state, 10000, 10000])

        for state in scores:
            print("evaluating")
            if state not in openSet:
                openSet.append(state)

            gScore = current[2] + depth
            #if gScore >= state[2]:
                #continue
            cameFrom.append(current)
            state[2] = gScore
            state[1] = gScore + solve.hs(state[0])
    
        depth = depth + 1
   
def solve_ball_a(this_ball):

    done = False
    current = [this_ball, solve.hs(this_ball), 10000]
    path = []
    depth = 0
    backtrack = False
    counter = 0
    while not done:

        path.append(current) 

        if current[1] < 47:
            print("solved")
            return path

        # expand nodes
        if backtrack == False: 
            states = build_possible_state_branch(current[0])
            state_scores = []
            for state in states:
                state_scores.append([state, solve.hs(state), depth])
        else:
            backtrack == True

        print(counter)
        print(len(state_scores))

        found = False
        for state_score in state_scores:
            print(state_score[1])
            if state_score[1] < current[1]:
                current = state_score
                found = True


        if found == False:
            if state_scores[0][1] == 1000 and state_scores[1][1] == 1000 and state_scores[2][1] == 1000 and state_scores[3][1] == 1000:
                current = path[depth-2]
            else:            
                counter = counter + 1
                backtrack = True
                bad = current[0].rows
                current = path[depth-1]
                current[1] = 10000
                states = build_possible_state_branch(current[0])
                state_scores = []
                for state in states:
                    if bad != state.rows:
                        state_scores.append([state, solve.hs(state), depth])
                    else: 
                        state_scores.append([state, 1000, depth])

                path.pop()

        depth = depth + 1
        if depth == 100:
            print("solving failed")
            break

def main():
    if len(sys.argv) < 2 or len(sys.argv) >= 6:
        print("Usage: ")
        print("         python run.py [number of random moves to generate]")
        print("         python run.py [row to move] [direction] [row to hold]")
        print("         python run,py [row to move] [direction] [row to hold] [quit after execute, don't wait for more input]")
    elif len(sys.argv) == 2:
        randomize_quick(int(sys.argv[1]))
    elif len(sys.argv) == 3:
        randomize_state(int(sys.argv[1]))
    elif len(sys.argv) > 3 and len(sys.argv) < 6:
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
    #main()
    our_ball = ball()
    our_ball = randomize_quick(3, True)
    solved_path = solve_ball_a(our_ball)
    for item in solved_path:
        item[0].output_ball()



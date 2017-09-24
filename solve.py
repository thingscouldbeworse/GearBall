from ball import ball
import util
from pprint import pprint

# return the maximum number of turns for the pieces
# of a ball away from a solved state
def calc_max_dist(our_ball):
    for face in our_ball.faces:
        for piece in our_ball.faces[face].pieces:
            print(our_ball.faces[face].pieces[piece].text)

def find_center_by_color(color, ball):
    for face in ball.faces:
        if ball.faces[face].pieces['center'].color == color:
            return face

def find_center_by_color_3d(color, threedee):
    center_coords = [[0,2,2],[4,2,2],[2,0,2],[2,4,2],[2,2,0],[2,2,4]]
    for coord in center_coords:
        if threedee[coord[0]][coord[1]][coord[2]].color == color:
            return coord

def create_3d_ball(this_ball):
    threedee = [[[0 for k in range(0,5)] for j in range(0,5)] for i in range(0,5)] 
    
    for y in range(0,3):
        for z in range(0,3):
            threedee[0][y+1][z+1] = this_ball.faces['face_3'].pieces_by_grid(y,z)

    for y in range(0,3):
        for z in range(0,3):
            threedee[4][y+1][z+1] = this_ball.faces['face_6'].pieces_by_grid(y,z)

    for x in range(0,3):
        for z in range(0,3):
            threedee[x+1][0][z+1] = this_ball.faces['face_2'].pieces_by_grid(x,z)

    for x in range(0,3):
        for z in range(0,3):
            threedee[x+1][4][z+1] = this_ball.faces['face_4'].pieces_by_grid(x,z)

    for x in range(0,3):
        for y in range(0,3):
            threedee[x+1][y+1][0] = this_ball.faces['face_1'].pieces_by_grid(x, 2-y)
    
    for x in range(0,3):
        for y in range(0,3):
            threedee[x+1][y+1][4] = this_ball.faces['face_5'].pieces_by_grid(x,y)
    
    return threedee

our_ball = ball()
our_ball.move('top', 'left', 'center')
our_ball.move('left', 'up', 'center')
our_ball.output_ball()
threedee = create_3d_ball(our_ball)
print(find_center_by_color_3d('blue', threedee))


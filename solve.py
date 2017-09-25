from ball import ball
import util
from pprint import pprint

def hs(this_ball):
    threedee = create_3d_ball(this_ball)
    total_distance = 0
    for x in range(1,4):
        for y in range(1,4):
            total_distance = total_distance + piece_distance(x, y, 0, threedee)
            total_distance = total_distance + piece_distance(x, 0, y, threedee)
            total_distance = total_distance + piece_distance(0, x, y, threedee)
    for gear in this_ball.gears:
        total_distance = total_distance + this_ball.gears[gear].orientation - 1
    return total_distance

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
            threedee[4][y+1][z+1] = this_ball.faces['face_6'].pieces_by_grid(y,2-z)

    for x in range(0,3):
        for z in range(0,3):
            threedee[x+1][0][z+1] = this_ball.faces['face_2'].pieces_by_grid(2-x,z)

    for x in range(0,3):
        for z in range(0,3):
            threedee[x+1][4][z+1] = this_ball.faces['face_4'].pieces_by_grid(x,z)

    for x in range(0,3):
        for y in range(0,3):
            threedee[x+1][y+1][0] = this_ball.faces['face_1'].pieces_by_grid(y, 2-x)
    
    for x in range(0,3):
        for y in range(0,3):
            threedee[x+1][y+1][4] = this_ball.faces['face_5'].pieces_by_grid(y,x)
    
    return threedee

def piece_distance(x, y, z, threedee):

    piece1 = threedee[x][y][z]
    match_center = find_center_by_color_3d(piece1.color, threedee)
    target_coords = [-1,-1,-1]
    for i in range(0,3):
        if match_center[i] == 4 or match_center[i] == 0:
            target_coords[i] = match_center[i]
            break
    # left and right
    if i == 2: # faces 1 and 5
        if "left" in piece1.style:
            target_coords[1] = 1
        elif "right" in piece1.style:
            target_coords[1] = 3
        else:
            target_coords[1] = 2
    elif i == 1: #faces 2 and 4
        if "left" in piece1.style:
            if match_center[i] == 0:
                target_coords[0] = 3
            elif match_center[i] == 4:
                target_coords[0] = 1
        elif "right" in piece1.style:
            if match_center[i] == 0:
                target_coords[0] = 1
            elif match_center[i] == 4:
                target_coords[0] = 3
        else:
            target_coords[0] = 2
    elif i == 0: # faces 3 and 6
        if "left" in piece1.style:
            target_coords[1] = 1
        elif "right" in piece1.style:
            target_coords[1] = 3
        else:
            target_coords[1] = 2
       
    # top and bottom
    if i == 2:
        target_coords[2] = match_center[2]
        if "top" in piece1.style and match_center[2] == 0:
            target_coords[0] = 3
        elif "top" in piece1.style and match_center[2] == 4:
            target_coords[0] = 1
        elif "bottom" in piece1.style and match_center[2] == 0:
            target_coords[0] = 1
        elif "bottom" in piece1.style and match_center[2] == 4:
            target_coords[0] = 3
        else:
            target_coords[0] = 2
    else:
        if "top" in piece1.style:
            target_coords[2] = 1
        elif "bottom" in piece1.style:
            target_coords[2] = 3
        else:
            target_coords[2] = 2
    return util.distance([x,y,z], target_coords)


our_ball = ball()
our_ball.move('top', 'left', 'center')
our_ball.move('left', 'up', 'center')
our_ball.output_ball()
print(hs(our_ball))
#threedee = create_3d_ball(our_ball)
#print(piece_distance(1,2,0,threedee))



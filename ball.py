import copy
from ball_components import face, piece, gear
import util

class ball:

    def __init__(self, scrambled=False):
        self.faces = {
            'face_1':   face('purple', 1),
            'face_2':   face('cyan', 2),
            'face_3':   face('green', 3),
            'face_4':   face('magenta', 4),
            'face_5':   face('red', 5),
            'face_6':   face('blue', 6),
            }
        self.rows = []
        self.gears = {
                '1a':  gear(self.faces['face_1'].color, self.faces['face_6'].color, 'gear_1a'),
                '1b':  gear(self.faces['face_1'].color, self.faces['face_3'].color, 'gear_1b'),
                '2a':  gear(self.faces['face_2'].color, self.faces['face_1'].color, 'gear_2a'),
                '2b':  gear(self.faces['face_2'].color, self.faces['face_5'].color, 'gear_2b'),
                '3a':  gear(self.faces['face_3'].color, self.faces['face_4'].color, 'gear_3a'),
                '3b':  gear(self.faces['face_3'].color, self.faces['face_2'].color, 'gear_3b'),
                '4a':  gear(self.faces['face_4'].color, self.faces['face_1'].color, 'gear_4a'),
                '4b':  gear(self.faces['face_4'].color, self.faces['face_5'].color, 'gear_4b'),
                '5a':  gear(self.faces['face_5'].color, self.faces['face_3'].color, 'gear_5a'),
                '5b':  gear(self.faces['face_5'].color, self.faces['face_6'].color, 'gear_5b'),
                '6a':  gear(self.faces['face_6'].color, self.faces['face_4'].color, 'gear_6a'),
                '6b':  gear(self.faces['face_6'].color, self.faces['face_2'].color, 'gear_6b')
                }

        self.textify_rows()

    def textify_rows(self):

        self.rows = []

        # face1 and gear1a
        self.rows.append("     " + self.gears['1a'].text)
        self.append_row_with_space(1)
        #gears 2a, 3a, 4a
        self.rows.append(" " + self.gears['2a'].text + "   " + self.gears['1b'].text + "   " + self.gears['4a'].text)

        row1, row2, row3 = self.faces['face_2'].return_output_all()
        text_row1 = row1 + " "
        text_row2 = row2 + self.gears['3b'].text
        text_row3 = row3 + " "

        row1, row2, row3 = self.faces['face_3'].return_output_all()
        text_row1 = text_row1 + row1 + " "
        text_row2 = text_row2 + row2 + self.gears['3a'].text
        text_row3 = text_row3 + row3 + " "

        row1, row2, row3 = self.faces['face_4'].return_output_all()
        text_row1 = text_row1 + row1
        text_row2 = text_row2 + row2
        text_row3 = text_row3 + row3

        self.rows.append(text_row1)
        self.rows.append(text_row2)
        self.rows.append(text_row3)

        self.rows.append(" " + self.gears['2b'].text + "   " + self.gears['5a'].text + "   " + self.gears['4b'].text)

        self.append_row_with_space(5)
        self.rows.append("     " + self.gears['5b'].text)

        row1, row2, row3 = self.faces['face_6'].return_output_all()
        self.rows.append("    " + row1)
        self.rows.append("   " + self.gears['6b'].text + row2 + self.gears['6a'].text)
        self.rows.append("    " + row3)

    def append_row_with_space(self, row_number):

        row1, row2, row3 = self.faces['face_'+str(row_number)].return_output_all()
        self.rows.append("    " + row1)
        self.rows.append("    " + row2)
        self.rows.append("    " + row3)

    def output_ball(self):

        self.textify_rows()
        for row in self.rows:
            print(row)
 
    def move(self, row, direction, hold):
        
        print("Moving the " + row + " row " + direction + " while holding the " + hold + " row.")
        real_direction = 'none'
        if hold == 'center':
            if direction == 'right':
                opposite_direction = 'left'
            elif direction == 'left':
                opposite_direction = 'right'
            elif direction == 'up':
                opposite_direction = 'down'
            elif direction == 'down':
                opposite_direction = 'up'
            
            if row == 'top':
                real_direction = direction
                opposite_row = 'bottom'
            elif row == 'bottom':
                real_direction = opposite_direction
                opposite_direction = direction
                opposite_row = 'top'
            elif row == 'left':
                real_direction = direction
                opposite_row = 'right'
            elif row == 'right':
                real_direction = opposite_direction
                opposite_direction = direction
                opposite_row = 'left'
        else:
            move = 'double'
            if direction == 'right' or direction == 'up':
                increment = 1
            elif direction == 'left' or direction == 'down':
                increment = -1
            if row == 'top':
                self.rotate_edge('1', direction)
                self.rotate_edge('1', direction)
            elif row == 'bottom':
                self.rotate_edge('5', direction)
                self.rotate_edge('5', direction)
                increment = increment * -1
            elif row == 'left':
                self.rotate_edge('2', direction)
                self.rotate_edge('2', direction)
            elif row == 'right':
                self.rotate_edge('4', direction)
                self.rotate_edge('4', direction)
                increment = increment * -1

            # two moves for the row because we're not holding center
            self.full_row_move(row, direction)
            self.full_row_move(row, direction)

            if direction == 'right' or direction == 'left': 
                self.full_gear_update(increment, 'x')
            elif direction == 'up' or direction == 'down':
                self.full_gear_update(increment, 'z')

            self.full_row_move('center', direction)

        if real_direction == 'right' or real_direction == 'up':
            increment = 1
        elif real_direction == 'left' or real_direction == 'down':
            increment = -1

        if real_direction == 'right' or real_direction == 'left':
            self.full_row_move('top', real_direction)
            self.rotate_edge('1', real_direction)
            
            self.full_row_move('bottom', opposite_direction)
            self.rotate_edge('5', real_direction)
            
            self.full_gear_update(increment, 'x')
        elif real_direction == 'up' or real_direction == 'down':
            self.full_row_move('left', real_direction)
            self.rotate_edge('2', real_direction)

            self.full_row_move('right', opposite_direction)
            self.rotate_edge('4', real_direction)

            self.full_gear_update(increment, 'z')
         

    def full_row_move(self, row, direction):
        face_dict = {
                    'x': ['face_3', 'face_2', 'face_6', 'face_4'],
                    'z': ['face_3', 'face_5', 'face_6', 'face_1']
                    }
        gear_dict = {
                    'x': ['3b', '6b', '6a', '3a'],
                    'z': ['1b', '5a', '5b', '1a']
                    }
        if direction == 'left' or direction == 'right':
            axis = 'x'
            face_list = face_dict[axis]
            # inflect face 6 
            self.faces['face_6'].inflect()

        elif direction == 'up' or direction == 'down':
            axis = 'z'
            face_list = face_dict[axis]
                                
        if direction == 'left' or direction == 'down':
            face_list = list(reversed(face_list))

        self.faces['temp_face'] = copy.deepcopy(self.faces[face_list[0]])
        face_list.append('temp_face')
        
        for i in range(0,4):
            self.faces[face_list[i]] = move_row_pieces(self.faces[face_list[i+1]], self.faces[face_list[i]], row, axis) 
       
        self.faces.pop('temp_face', None)
        
        if row == 'center':
            # also do gear position updates for center moves
            if direction == 'right':
                gear_list = gear_dict['x']
            elif direction == 'right':
                gear_list = list(reversed(gear_dict['x']))
            elif direction == 'up':
                gear_list = gear_dict['z']
            elif direction == 'down':
                gear_list = list(reversed(gear_dict['z']))

            temp_gear = copy.deepcopy(self.gears[gear_list[0]])
            self.gears['temp_gear'] = temp_gear
            gear_list.append('temp_gear')
            
            for i in range(0, 4):
                self.gears[gear_list[i]] = copy.deepcopy(self.gears[gear_list[i+1]])
            self.gears.pop('temp', None)

        if direction == 'left' or direction == 'right':
            # inflect face_6 back 
            self.faces['face_6'].inflect()


    def full_gear_update(self, increment, axis):
        gear_dict = {
                    'x': ['3a', '3b', '6a', '6b'],
                    'y': ['2a', '2b', '4a', '4b'],
                    'z': ['1a', '1b', '5a', '5b']
                    }
        
        gear_list = gear_dict[axis]
        for i in range(0,4):
            self.gears[gear_list[i]].adjust_orientation(self.gears[gear_list[i]].orientation + increment)

    def rotate_edge(self, edge, direction):
        
        face = self.faces['face_' + edge]
        gear_dict = { 
                    '1': ['1a', '4a', '1b', '2a'],
                    '5': ['5a', '4b', '5b', '2b'],
                    '2': ['2a', '3b', '2b', '6b'],
                    '4': ['4a', '6a', '4b', '3a']
                    }
        # gears
        
        gear_list = gear_dict[edge]
        
        if direction == 'left' or direction == 'down':
            gear_list = list(reversed(gear_list))
        
        temp_gear = copy.deepcopy(self.gears[gear_list[0]])
        self.gears['temp'] = temp_gear
        gear_list.append('temp')
        
        for i in range(0,4):
            self.gears[gear_list[i]] = copy.deepcopy(self.gears[gear_list[i+1]])

        self.gears.pop('temp', None)
   
        # counter-clockwise
        if direction == 'right' or direction == 'up':
            # corners
            temp_piece = copy.deepcopy(face.pieces['top_right'])
            face.pieces['top_right'] = copy.deepcopy(face.pieces['bottom_right'])
            face.pieces['bottom_right'] = copy.deepcopy(face.pieces['bottom_left'])
            face.pieces['bottom_left'] = copy.deepcopy(face.pieces['top_left'])
            face.pieces['top_left'] = copy.deepcopy(temp_piece)
            # inner pieces
            temp_piece = copy.deepcopy(face.pieces['right'])
            face.pieces['right'] = copy.deepcopy(face.pieces['bottom'])
            face.pieces['bottom'] = copy.deepcopy(face.pieces['left'])
            face.pieces['left'] = copy.deepcopy(face.pieces['top'])
            face.pieces['top'] = copy.deepcopy(temp_piece)
        # clockwise
        elif direction == 'left' or direction == 'down':
            # corners
            temp_piece = copy.deepcopy(face.pieces['top_right'])
            face.pieces['top_right'] = copy.deepcopy(face.pieces['top_left'])
            face.pieces['top_left'] = copy.deepcopy(face.pieces['bottom_left'])
            face.pieces['bottom_left'] = copy.deepcopy(face.pieces['bottom_right'])
            face.pieces['bottom_right'] = copy.deepcopy(temp_piece)
            # inner pieces
            temp_pieces = copy.deepcopy(face.pieces['right'])
            face.pieces['right'] = copy.deepcopy(face.pieces['top'])
            face.pieces['top'] = copy.deepcopy(face.pieces['left'])
            face.pieces['left'] = copy.deepcopy(face.pieces['bottom'])
            face.pieces['bottom'] = copy.deepcopy(temp_piece)

def move_row_pieces(first, second, row, axis = 'x'):

    if axis == 'z' and row == 'center':
        piece1 = 'bottom'
        piece2 = 'center'
        piece3 = 'top'
    elif axis == 'x' and row == 'center':
        piece1 = 'left'
        piece2 = 'center'
        piece3 = 'right'
    elif row == 'top' or row == 'bottom':
        piece1 = row + '_left'
        piece2 = row
        piece3 = row + '_right'
    elif row == 'left' or row == 'right':
        piece1 = 'bottom_' + row
        piece2 = row
        piece3 = 'top_' + row
 
    second.pieces[piece1].change_color(first.pieces[piece1].color)
    second.pieces[piece2].change_color(first.pieces[piece2].color)
    second.pieces[piece3].change_color(first.pieces[piece3].color)

    return second


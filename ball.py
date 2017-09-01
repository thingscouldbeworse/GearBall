import util
import copy

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
                opposite_row = 'top'
            elif row == 'left':
                real_direction = direction
                opposite_row = 'right'
            elif row == 'right':
                real_direction = opposite_direction
                opposite_row = 'left'
        else:
            move = hold + "_" + row + "_" + direction

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
        if direction == 'left' or direction == 'right':
            face_list = face_dict['x']
            # inflect face 6 
            self.faces['face_6'].inflect()

        elif direction == 'up' or direction == 'down':
            face_list = face_dict['z']
                                
        if direction == 'left' or direction == 'down':
            face_list = list(reversed(face_list))

        self.faces['temp_face'] = copy.deepcopy(self.faces[face_list[0]])
        face_list.append('temp_face')
        
        for i in range(0,4):
            self.faces[face_list[i]] = move_row_pieces(self.faces[face_list[i+1]], self.faces[face_list[i]], row) 
       
        self.faces.pop('temp_face', None)

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
        
        # counter-clockwise
        if direction == 'right' or direction == 'up':
            temp_piece = copy.deepcopy(face.pieces['top_right'])
            face.pieces['top_right'] = copy.deepcopy(face.pieces['bottom_right'])
            face.pieces['bottom_right'] = copy.deepcopy(face.pieces['bottom_left'])
            face.pieces['bottom_left'] = copy.deepcopy(face.pieces['top_left'])
            face.pieces['top_left'] = copy.deepcopy(temp_piece)
            temp_piece = copy.deepcopy(face.pieces['right'])
            face.pieces['right'] = copy.deepcopy(face.pieces['bottom'])
            face.pieces['bottom'] = copy.deepcopy(face.pieces['left'])
            face.pieces['left'] = copy.deepcopy(face.pieces['top'])
            face.pieces['top'] = copy.deepcopy(temp_piece)
        # clockwise
        elif direction == 'left' or direction == 'down':
            temp_piece = copy.deepcopy(face.pieces['top_right'])
            face.pieces['top_right'] = copy.deepcopy(face.pieces['top_left'])
            face.pieces['top_left'] = copy.deepcopy(face.pieces['bottom_left'])
            face.pieces['bottom_left'] = copy.deepcopy(face.pieces['bottom_right'])
            face.pieces['bottom_right'] = copy.deepcopy(temp_piece)
            temp_pieces = copy.deepcopy(face.pieces['right'])
            face.pieces['right'] = copy.deepcopy(face.pieces['top'])
            face.pieces['top'] = copy.deepcopy(face.pieces['left'])
            face.pieces['left'] = copy.deepcopy(face.pieces['bottom'])
            face.pieces['bottom'] = copy.deepcopy(temp_piece)






class face:

    position = 0
    def __init__(self, color, position):

        # 4 corners, 4 edges, 1 center, gears are handled at the ball level
        # because faces don't know which faces they border
        self.pieces = {
                'top_right': piece(color, 'top_right'),
                'top_left': piece(color, 'top_left'),
                'bottom_right': piece(color, 'bottom_right'),
                'bottom_left': piece(color, 'bottom_left'),
                'left': piece(color, 'left'),
                'right': piece(color, 'right'),
                'top': piece(color, 'top'),
                'bottom': piece(color, 'bottom'),
                'center': piece(color, 'center')
                }
        self.position = position
        self.color = color

    def return_individual(self, piece):
        return self.pieces[piece]

    def return_all(self):
        return self.pieces

    def output_individual(self, piece):
        piece = self.pieces[piece]
        return piece.text

    def output_all(self):
        top_row     = self.pieces['top_left'].text + self.pieces['top'].text + self.pieces['top_right'].text
        middle_row  = self.pieces['left'].text + self.pieces['center'].text + self.pieces['right'].text
        bottom_row  = self.pieces['bottom_left'].text + self.pieces['bottom'].text + self.pieces['bottom_right'].text
        print(top_row)
        print(middle_row)
        print(bottom_row)

    def return_output_all(self):
        top_row     = self.pieces['top_left'].text + self.pieces['top'].text + self.pieces['top_right'].text
        middle_row  = self.pieces['left'].text + self.pieces['center'].text + self.pieces['right'].text
        bottom_row  = self.pieces['bottom_left'].text + self.pieces['bottom'].text + self.pieces['bottom_right'].text

        return [top_row, middle_row, bottom_row]

    def inflect(self):
        temp_piece = copy.deepcopy(self.pieces['top_right'])
        self.pieces['top_right'] = copy.deepcopy(self.pieces['bottom_left'])
        self.pieces['bottom_left'] = copy.deepcopy(temp_piece)
        temp_piece = copy.deepcopy(self.pieces['top_left'])
        self.pieces['top_left'] = copy.deepcopy(self.pieces['bottom_right'])
        self.pieces['bottom_right'] = copy.deepcopy(temp_piece)
        temp_piece = copy.deepcopy(self.pieces['top'])
        self.pieces['top'] = copy.deepcopy(self.pieces['bottom'])
        self.pieces['bottom'] = copy.deepcopy(temp_piece)
        temp_piece = copy.deepcopy(self.pieces['left'])
        self.pieces['left'] = copy.deepcopy(self.pieces['right'])
        self.pieces['right'] = copy.deepcopy(temp_piece)


class piece:

    text = '▆'
    def __init__(self, color, style):
        self.color = color
        self.type = style
        self.text = util.color_sub(color, self.text)

    def change_color(self, new_color):
        self.text = util.color_sub(new_color, self.text)
        self.color = new_color

class gear:

    text = '1'
    def __init__(self, color1, color2, name):
        self.name = name
        self.color1 = color1
        self.color2 = color2
        self.orientation = 1
        self.text = util.color_sub_gear(color1, color2, str(self.orientation))
    
    def adjust_orientation(self, new_orientation):
        if new_orientation == 0:
            new_orientation = 6
        elif new_orientation == 7:
            new_orientation = 1
        self.orientation = new_orientation
        self.text = util.color_sub_gear(self.color1, self.color2, str(new_orientation))

def vertical_move(ball, direction, row, hold):
    
    print("executing a vertical move " + direction + " on the " + row + " row while holding the " + hold + " row.")

def move_row_pieces(first, second, row):

    if row == 'center':
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


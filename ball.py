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
        self.rows.append("    " + row3)
        self.rows.append("   " + self.gears['6b'].text + row2 + self.gears['6a'].text)
        self.rows.append("    " + row1)

    def append_row_with_space(self, row_number):

        row1, row2, row3 = self.faces['face_'+str(row_number)].return_output_all()
        self.rows.append("    " + row1)
        self.rows.append("    " + row2)
        self.rows.append("    " + row3)

    def output_ball(self):

        for row in self.rows:
            print(row)
 
    def horizontal_move(self, direction, row, hold):
        
        print("executing a horizontal move to the " + direction + " on the " + row + " row while holding the " + hold + " row.")
        # holding opposite moves: 
        #   horizontal face equivalent rows switch (move two rotations)
        #   horizontal face center rows move one face in <direction>
        #   horizontal gears move 1 step in <direction> and change 1 in orientation (increment for right, decrement for left)
        # holding center moves:
        #   hold moves one face in opposite
        #   row moves one face in <direction>
        #   all horizontal equivalents move simmilarly
        #   all horizontal gears stay in the same position and change 1 orientation
        #   orientation follows up, left for decrement, right for increment

        if hold == 'center':
            if row == 'top':
                if direction == 'left':
                    move = 'left'
                elif direction == 'right':
                    move = 'right'
            elif row == 'bottom':
                if direction == 'left':
                    move = 'right'
                elif direction == 'right':
                    move = 'left'
        else:
            move = hold + "_" + row + "_" + direction

        if move == 'right':
            # move top row around
            self.full_row_move_horizontal('top', 'right')

            # move bottom row around in opposite direction 
            self.full_row_move_horizontal('bottom', 'left')

            # adjust gear orientations
            self.full_gear_update(1, 'x')

        elif move == 'left':
            # move top row around
            self.full_row_move_horizontal('top', 'left')

            # move bottom row around in opposite direction 
            self.full_row_move_horizontal('bottom', 'right')
            # adjust gear orientations
            self.full_gear_update(-1, 'x')
         

    def full_row_move_horizontal(self, row, direction):
        face_list = [
                'face_3',
                'face_2',
                'face_6',
                'face_4'
                ]
        if direction == 'left':
            face_list = list(reversed(face_list))

        self.faces['temp_face'] = copy.deepcopy(self.faces[face_list[0]])
        face_list.append('temp_face')
        
        for i in range(0,4):
            self.faces[face_list[i]] = move_row_pieces(self.faces[face_list[i+1]], self.faces[face_list[i]], row) 
       
        self.faces.pop('temp_face', None)

    def full_gear_update(self, increment, axis):
        gear_dict = {
                    'x': ['3a', '3b', '6a', '6b'],
                    'y': ['2a', '2b', '4a', '4b'],
                    'z': ['1a', '1b', '5a', '5b']
                    }
        
        gear_list = gear_dict[axis]
        for i in range(0,4):
            self.gears[gear_list[i]].adjust_orientation(self.gears[gear_list[i]].orientation + increment)

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
    else:
        piece1 = row + '_left'
        piece2 = row
        piece3 = row + '_right'
 
    second.pieces[piece1].change_color(first.pieces[piece1].color)
    second.pieces[piece2].change_color(first.pieces[piece2].color)
    second.pieces[piece3].change_color(first.pieces[piece3].color)

    return second


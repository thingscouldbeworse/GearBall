import util
import copy

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


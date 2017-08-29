import util

class ball:
    
    def __init__(self, scrambled=False):

        self.faces = {
                'purple_face':  face('purple', 1),
                'red_face':     face('red', 5),
                'green_face':   face('green', 3),
                'blue_face':    face('blue', 6),
                'magenta_face': face('magenta', 4),
                'cyan_face':    face('cyan', 2),
                }


class face:

    position = 0
    def __init__(self, color, position):

        # 4 corners, 4 edges, 1 center, 1 gear
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
        

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
                'gear_1':   gear(1, self.faces['face_1'].color, self.faces['face_6'].color),
                'gear_2':   gear(2, self.faces['face_2'].color, self.faces['face_1'].color),
                'gear_3':   gear(3, self.faces['face_3'].color, self.faces['face_1'].color),
                'gear_4':   gear(4, self.faces['face_4'].color, self.faces['face_1'].color),
                'gear_5':   gear(5, self.faces['face_5'].color, self.faces['face_3'].color)
                }

        self.textify_rows()
        
    def textify_rows(self): 
        
        self.append_row_with_space(1)

        row1, row2, row3 = self.faces['face_2'].return_output_all()
        text_row1 = row1
        text_row2 = row2
        text_row3 = row3
        
        row1, row2, row3 = self.faces['face_3'].return_output_all()
        text_row1 = text_row1 + row1
        text_row2 = text_row2 + row2
        text_row3 = text_row3 + row3

        row1, row2, row3 = self.faces['face_4'].return_output_all()
        text_row1 = text_row1 + row1
        text_row2 = text_row2 + row2
        text_row3 = text_row3 + row3

        self.rows.append(text_row1)
        self.rows.append(text_row2)
        self.rows.append(text_row3)

        self.append_row_with_space(5)

        self.append_row_with_space(6)
  
    def append_row_with_space(self, row_number):
        
        row1, row2, row3 = self.faces['face_'+str(row_number)].return_output_all()
        self.rows.append("   " + row1)
        self.rows.append("   " + row2)
        self.rows.append("   " + row3)

        
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

class gear:
    
    text = '1'
    def __init__(self, position, color1, color2):
        self.position = position
        self.color1 = color1
        self.color2 = color2
        self.orientation = 1
        self.text = str(self.orientation) 
 

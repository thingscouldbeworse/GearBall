import re 
import math

COLORS = dict(
        list(zip([
            'grey',
            'red',
            'green',
            'magenta',
            'blue',
            'purple',
            'cyan',
            'white'
            ],
            list(range(30, 38))
            ))
        )

COLORS_RE = '\033\[(?:%s)m' % '|'.join(['%d' % v for v in COLORS.values()])
RESET = '\033[0m'
RESET_RE = '\033\[0m'   
fmt_str = '\033[%dm%s'
endc = '\033[0m'

def color_sub(color, text):
 
    text = re.sub(COLORS_RE + '(.*?)' + RESET_RE, r'\1', text)
    text = fmt_str % (COLORS[color], text)
    text = text + endc
    return text

def color_sub_gear(color1, color2, text):

    color1 = COLORS[color1]
    color2 = COLORS[color2] + 10

    return '\033['+ str(color1) +';'+ str(color2) +'m' + text + '\033[0m'

def color_piece(color, text):
    
    return color_sub(color, piece.text)
   
    
def color_face(face):
    
    pieces = face.return_all()
    text = ""
 
def get_opposite(direction):
    
    opposite_dict = { 'right': 'left', 'left': 'right', 'up': 'down', 'down': 'up' }
    return opposite_dict[direction]

def get_opposing_face(face_num):
    if face_num == 1:
        return 5
    elif face_num == 2:
        return 4
    elif face_num == 3:
        return 6

def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2 + (p0[2] - p1[2])**2)

def style_to_coords(style):
    plcae = ""


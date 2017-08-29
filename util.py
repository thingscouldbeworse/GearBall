import re

COLORS = dict(
        list(zip([
            'grey',
            'red',
            'green',
            'purple',
            'blue',
            'magenta',
            'cyan',
            'white'
            ],
            list(range(30, 38))
            ))
    )


def color_sub(color, text):
 
    COLORS_RE = '\033\[(?:%s)m' % '|'.join(['%d' % v for v in COLORS.values()])
    RESET = '\033[0m'
    RESET_RE = '\033\[0m'   
    fmt_str = '\033[%dm%s'

    text = re.sub(COLORS_RE + '(.*?)' + RESET_RE, r'\1', text)
    text = fmt_str % (COLORS[color], text)
    text = text + '\033[0m'
    return text


def color_piece(color, text):
    
    return color_sub(color, piece.text)
   
    
def color_face(face):
    
    pieces = face.return_all()
    text = "" 
    
   

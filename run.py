from ball import ball, face, piece, gear
import util
import sys

our_ball = ball()
state = our_ball.rows
for item in state:
    print(item)

gear1 = gear('red', 'green', 1)
gear1.text = util.color_sub_gear('red', 'magenta', '2')
print(gear1.text)


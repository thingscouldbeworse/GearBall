from ball import ball, face, piece, gear
import util
import sys

our_ball = ball()
our_ball.output_ball()
our_ball.move('top', 'right', 'center')
our_ball.output_ball()

our_ball.move('left', 'up', 'center')
our_ball.output_ball()

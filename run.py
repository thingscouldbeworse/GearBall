
from ball import ball
from ball_components import face, piece, gear
import util
import sys

our_ball = ball()
our_ball.output_ball()
our_ball.move('right', 'up', 'left')
our_ball.output_ball()

our_ball.move('right', 'up', 'left')
our_ball.output_ball()


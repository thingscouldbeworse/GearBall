# Gearball simulator 

## Usage

invoke the gear ball randomizer with 

```zsh
python run.py [number]
```
where [number] is the number of moves you want the randomizer to take. Each moven taken will print the steps taken (row moved, direction moved in, row held) and the state of the gear ball after the move.

If you wish to make a single move on the gearball invoke `run.py` via
```zsh
python run.py [row to move] [direction to move in] [row to hold] [q to quit]
```

For example, to execute a left twist on the top row while moving the bottom row in the opposite direction (the center row does not move), you would use

```zsh
python run.py top left center q
```

If you want to continue to make moves on the gear ball after your initial move do not append 'q' to the end of your arguments. Continue to move the gear ball via the same command structure, `[row] [direction] [hold]`. Type `quit` or `q` to exit the gearball program.

The state of the gearball will be output to the screen after each move.

## GUI

The gearball output is colored with 6 colors, one for each face of the gearball;
```
    purple
    cyan
    green
    magenta
    red
    blue
```

The central face (the one at the center of the "cross" formed by unfolding the gearball) is the face on which operations are executed upon, ie one row of the central face (left, right, top, or bottom) will always stay central. 

A solved (or untouched) gearball will look like this:

![screenshot](https://raw.githubusercontent.com/thingscouldbeworse/gearball/master/solved_example.png)

and a gearball with one move executed (a left move up while holding center) will look like this:

![screenshot](https://raw.githubusercontent.com/thingscouldbeworse/gearball/master/1move_example.png)

## Data Structure

A 'Gearball is an object defined in the `ball` class found in `ball.py`. A gearball has a collection of functions to print the state of the current gearball to the screen (textify_rows, output_ball, etc), and dicts of the other objects included within the ball. These are `rows` (the string version of the ball, only used to display the gearball state), `faces` (6, numbered, the six faces of a gearball) and `gears` (12, the gear pieces in between each face. Each faces and gears dict consists of keys corresponding to the location of the object on the gearball in string form, and the reference to that object as the value.

Faces and gears are python objects as well. Gears have an orientation and two colors, the two colors coming from the two faces the gear borders, and the orientation referencing which cog is pointing to the right. This orientation is numbered 1 to 6, with 1 being the 'solved' state of the gear (the state it begins in). Both colors are one of the possible 6 (purple, cyan, etc), given at gear creation. The string representation of the gear has the orientation colored as color 1 (one of the bordered faces) and the background as color 2 (the other bordered face). Gears never change color, they only change location on the ball (kept track of at the `ball` level object) and their orientation is updated as the adjacent rows slide past.

Faces have a dict of `piece` objects, another python object, and some functions used to output the state of the face. Color is handled at the `piece` level, faces only keep track of which pieces they own.

The `piece` object knows its own color and possesses a function to change its color to a new color. The location of each piece is kept track of at the `face` level, through the `pieces` dict. 

As move operations are performed on the central face, rows in adjacent faces have their pieces change color accordingly. Pieces never move position only color, and always belong to their original face. Gears will change position and orientation as needed.

## Randomizer

The `randomize()` function takes a number of moves as an argument, creates a gearball object, and scrambles it by generating sequential moves (up to the number passed to the function). This is accomplished by generating 3 random numbers, first to decide on a random row to move, then to decide a random direction, and finally a random row to hold. There are 16 "possible moves" (four rows, two directions, two holds, 4 * 2 * 2) but 8 of these moves are equivalent (`top left center` is equivalent to `bottom right center`) so 4 moves are removed from the possible moveset to avoid duplicates. 

The `randomize()` function also will not produce an "undo" move, moves that either directly return to the n-2 state (a 'top, right, center' move will not be immediately preceded by a 'top, left, center' move) or moves that would constitute a 90 or 180 degree turn (a 'top, right, bottom' and 'bottom, right, center' would simply result in the gearball being turned 90 degrees to the right). This is accomplished by storing the previous states of the gearball just before each move is taken and persisting this into the next iteration of the loop that chooses moves. A move is chosen (via  generating random numbers for th row, direction, and hold) and a temporary gear ball created from the state of the current gearball is moved according to the randomly chosen move. This temporary gearball's state (the string representation) is compared to the previous gearball's state and if they are equivalent, a new random move is generated. Simmilarly, before a move is executed the rotation states are saved (6 rotation states, 2 180 degree rotations on the x and y axis, 4 90 degree rotations towards 'up', 'left', 'right', 'down') and next iteration the possible move is compared against these possible rotations states, and a new random move is chosen if one is equal.


## Heuristic

## Statement



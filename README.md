# Gearball simulator 

## Usage

invoke the gear ball randomizer with 

```python
python run.py [number]
```
where [number] is the number of moves you want the randomizer to take. Each moven taken will print the steps taken (row moved, direction moved in, row held) and the state of the gear ball after the move.

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

A 'Gearball is an object defined in the `gearball` class found in `ball.py`. A gearball has a collection of functions to print the state of the current gearball to the screen (textify_rows, output_ball, etc), and dicts of the other objects included within the ball. These are `rows` (the string version of the ball, only used to display the gearball state), `faces` (6, numbered, the six faces of a gearball) and `gears` (12, the gear pieces in between each face. Each faces and gears dict consists of keys corresponding to the location of the object on the gearball in string form, and the reference to that object as the value.

Faces and gears are python objects as well. Gears have an orientation and two colors, the two colors coming from the two faces the gear borders, and the orientation referencing which cog is pointing to the right. This orientation is numbered 1 to 6, with 1 being the 'solved' state of the gear (the state it begins in). Both colors are one of the possible 6 (purple, cyan, etc), given at gear creation. The string representation of the gear has the orientation colored as color 1 (one of the bordered faces) and the background as color 2 (the other bordered face). Gears never change color, they only change location on the ball (kept track of at the `ball` level object) and their orientation is updated as the adjacent rows slide past.

Faces have a dict of `piece` objects, another python object, and some functions used to output the state of the face. Color is handled at the `piece` level, faces only keep track of which pieces they own.

The `piece` object knows its own color and possesses a function to change its color to a new color. The location of each piece is kept track of at the `face` level, through the `pieces` dict. 

As move operations are performed on the central face, rows in adjacent faces have their pieces change color accordingly. Pieces never move position only color, and always belong to their original face. Gears will change position and orientation as needed.

## Randomizer

## Heuristic

## Statement



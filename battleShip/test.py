"""
ship_loc = None
while ship_loc is None:
    input_loc = input("Please enter the location of the ship: ")
    try:
        # try and convert the string input to a number
        age = int(input_value)
    except ValueError:
        # tell the user off
        print("{input} is not a number, please enter a number only".format(input=input_value))
if age >= 18:
    print("You are able to vote in the United States!")
else:
    print("You are not able to vote in the United States.")
"""

"""
class GameLoopError(Exception):
    def __init__(self, reason: str) -> None:
        self.reason = reason

    def __str__(self) -> str:
        return self.reason


# suppose accepted a string format of "1, 2"
ncol = 9
nrow = 9
ship_loc = None
while ship_loc is None:
    input_loc = input("Please enter the location of the ship: ")
    # check the input is not in the form row, col
    try:
        row, col = input_loc.split(',')
    except ValueError:
        raise Exception(f'{input_loc} is not in the form row, col')

    # check either row or col is not an integer
    try:
        row = int(row)
    except ValueError:
        raise Exception(f'row needs to be an integer. {row} is not an integer')

    try:
        col = int(col)
    except ValueError:
        raise Exception(f'col needs to be an integer. {col} is not an integer')

    # check the coordinate is valid or not
    try:
        col >= ncol or col < 0
    except ValueError:
        raise Exception(f"Cannot place {self.ship_name} at column: {col} "
                        "because it would be out of bounds."
                        )
    try:
        row >= nrow or row < 0
    except ValueError:
        raise Exception(f"Cannot place {self.ship_name} at row: {row} "
                        "because it would be out of bounds."
                        )

    # check The ship is out of bound
    try:
        bool((row + size - 1 > self.nrow) * is_vertical +
            (col + size - 1 > self.ncol) * (1 - is_vertical))
    except ValueError:
        raise Exception(f"Cannot place {ship_name} {orientation}ly at col, row: {col}, {row} "
                        "because it would be out of bounds."
                        )
"""

from board import Board
from checking import LocationError, Validation
from player import Player
from ship import Ship
import sys
from sys import argv
from battleship import BattleShip


ship_list = []
ship_size_dict = {}
with open(argv[1], "r") as f:
    for i, line in enumerate(f):
        ship_size_dict[line.split()[0]] = line.split()[1]

test = BattleShip(9, 9)
test.ship_dict_loading(ship_size_dict)




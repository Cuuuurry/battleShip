
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

try:
    row, col = str_move.split(',')
except ValueError:
    raise MoveError(f'{str_move} is not in the form row, col')

try:
    row = int(row)
except ValueError:
    raise MoveError(f'row needs to be an integer. {row} is not an integer')

try:
    col = int(col)
except ValueError:
    raise MoveError(f'col needs to be an integer. {col} is not an integer')


# check the coordinate is valid or not
if col >= self.ncol or col < 0 or row >= self.nrow or row < 0:
    raise Exception("Cannot place {} {} at {}, {} "
                    "because it would be out of bounds."
                    .format(ship.ship_name, orientation, row, col))

# check The ship is out of bound
if bool((row + size - 1 > self.nrow) * is_vertical +
        (col + size - 1 > self.ncol) * (1 - is_vertical)):
    raise Exception("Cannot place {} {} at {}, {} "
                    "because it would be out of bounds.".format(ship.ship_name, orientation, row, col))
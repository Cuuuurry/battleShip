from typing import List
from board import Board
import random
from checking import Validation
from ship import Ship
from player import Player

class HumanPlayer(Player):
    def __init__(self, listed_ships: List[Ship]):
        super(HumanPlayer, self).__init__(self, listed_ships)
"""
This File:
    Ship information
        Count the fire
"""

form typing import List

# for ship in ship


class Ship(object):
    def __init__(self, ship_name, ship_size) -> None:
        self.ship_name = ship_name
        self.ship_size = ship_size
        self.ship_ori = None
        self.ship_loc = None

    def ship_oriented(self, orientation: str):
        self.ship_ori = orientation

    def ship_located(self, location: List[int]):
        self.ship_loc = location







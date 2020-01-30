"""
This File:
    Ship information
        Count the fire
"""

from typing import List

# for ship in ship


class Ship(object):
    def __init__(self, ship_name, ship_size) -> None:
        self.ship_name = ship_name
        self.ship_size = ship_size
        self.ship_ori = None
        self.ship_loc = None
        self.ship_health = ship_size

    def ship_oriented(self, orientation: str):
        # check orientation validation
        if orientation.lower() in {"vertical", "v", "ve", "ver", "vert", "verti", "vertic", "vertica"}:
            # set orientation
            self.ship_ori = "vertical"
        elif orientation.lower() in {"horizontal", "h", "ho", "hor", "hori", "horiz", "horizo", "horizon",
                                     "horizont", "horizonta", "horizontal"}:
            # set orientation
            self.ship_ori = "horizontal"
        else:
            raise Exception("{} does not represent an Orientation".format(orientation))

    def ship_located(self, location: List[int]):
        self.ship_loc = location

    def ship_health_change(self):
        self.ship_health -= 1

    def ship_destroyed(self):
        if not self.ship_health:
            return True
        else:
            return False


if __name__ == '__main__':
    S1 = Ship("monkey", 3)
    S1.ship_oriented("v")

"""
This File:
    Ship information
        Count the fire
"""

from typing import List, Tuple


class Ship(object):
    def __init__(self, ship_name, ship_size) -> None:
        self.ship_name = ship_name
        self.ship_size = ship_size
        self.ship_ori = None
        self.ship_loc = set()
        self.ship_health = ship_size

    def ship_oriented(self, orientation: str):
        # check orientation validation
        while True:
            if orientation.lower() in {"vertical", "v", "ve", "ver", "vert", "verti", "vertic", "vertica"}:
                # set orientation
                self.ship_ori = "vertical"
                break
            elif orientation.lower() in {"horizontal", "h", "ho", "hor", "hori", "horiz", "horizo", "horizon",
                                         "horizont", "horizonta", "horizontal"}:
                # set orientation
                self.ship_ori = "horizontal"
                break
            else:
                print("{} does not represent an Orientation".format(orientation))
                orientation = input("Please enter a valid orientation: ")


    def ship_located(self, location: Tuple[int]):
        self.ship_loc = set()
        self.ship_loc.add(location)
        index_dynamic = int(self.ship_ori == "horizontal")
        for i in range(self.ship_size):
            self.ship_loc.add(location[index_dynamic])

    def ship_health_change(self):
        self.ship_health -= 1

    def ship_destroyed(self):
        if not self.ship_health:
            return True
        else:
            return False


if __name__ == '__main__':
    S1 = Ship("monkey", 3)
    S1.ship_oriented("v ")

"""
This File:
    Ship information
        Count the fire
"""

from typing import Tuple, Any


class Ship(object):
    def __init__(self, ship_name: str, ship_size: int) -> None:
        self.ship_name = ship_name
        self.ship_size = ship_size
        self.ship_ori = None
        self.ship_loc = set()
        self.ship_health = ship_size

    def ship_oriented(self, orientation: str) -> bool:
        # check orientation validation
        ori = orientation.strip().lower()
        compare_num = len(ori)
        if ori == "vertical"[:compare_num]:
            # set orientation
            self.ship_ori = "vertical"
            return True
        elif ori == "horizontal"[:compare_num]:
            # set orientation
            self.ship_ori = "horizontal"
            return True
        else:
            print("{} does not represent an Orientation".format(orientation))
            return False

    def ship_located(self, location: Tuple[Any, Any]) -> None:
        self.ship_loc = set()
        self.ship_loc.add(location)
        for i in range(self.ship_size-1):
            if self.ship_ori == "horizontal":
                new_location = (location[0], location[1]+i+1)
                self.ship_loc.add(new_location)
            else:
                new_location = (location[0] + i + 1, location[1])
                self.ship_loc.add(new_location)

    def ship_health_change(self) -> None:
        self.ship_health -= 1

    def ship_destroyed(self) -> bool:
        if not self.ship_health:
            return True
        else:
            return False


if __name__ == '__main__':
    S1 = Ship("monkey", 3)
    S1.ship_oriented("v ")
    print(S1.ship_ori)

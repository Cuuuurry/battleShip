"""
This File:
    Board information
"""

from typing import Iterator, List


class Board(object):
    def __init__(self, num_rows: int, num_cols: int, is_scan: bool = False, blank_char: str = "*") -> None:
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.is_scan = is_scan
        if self.is_scan:
            self.scan_char = "(" + blank_char + ")"
        self.board = [[blank_char for col in range(num_cols)] for row in range(num_rows)]
        self.blank_char = blank_char

    def __str__(self):
        sep = ' ' * max([len(str(self.num_rows)), len(str(self.num_cols))]) + '\n'
        rep = sep + sep.join((str(i) for i in range(self.num_cols)))
        for row_index, row in enumerate(self):
            rep += str(row_index) + sep + sep.join(row) + '\n'
        return rep

    def __iter__(self) -> Iterator[List[str]]:
        return iter(self.board)


    def scan_or_place(self):
       pass

    #def





if __name__ == "__main__":
    board_case = Board(3,3)
    print(board_case)










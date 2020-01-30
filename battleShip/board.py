"""
This File:
    Board information
"""

from typing import Iterator, List


class Board(object):
    def __init__(self, num_rows: int, num_cols: int, blank_char: str = "*") -> None:
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.board = [[blank_char for col in range(num_cols)] for row in range(num_rows)]
        self.blank_char = blank_char

    def __str__(self):
        max_digit_num = max([len(str(self.num_rows)), len(str(self.num_cols))])
        sep = ' ' * max_digit_num #+ '\n'
        rep = sep
        for i in range(self.num_cols):
            rep += ' ' + ' ' * (max_digit_num - len(str(i))) + str(i)
        rep += "\n"
        for row_index, row in enumerate(self):
            num_of_space = max_digit_num - len(str(row_index))
            rep += ' ' * num_of_space + str(row_index) + sep + sep.join(row) + '\n'
        return rep

    def __iter__(self) -> Iterator[List[str]]:
        return iter(self.board)

    def __getitem__(self, row: int, col: int) -> List[str]:
        return self.board[row][col]

    def __setitem__(self, index, value):
        self.board[index[0]][index[1]] = value





if __name__ == "__main__":
    board_case = Board(13,13)
    print(board_case)










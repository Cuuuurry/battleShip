"""
This File:
    Board information
"""

from typing import Iterator, List


class Board(object):
    def __init__(self, num_rows: int, num_cols: int, blank_char: str = "*") -> None:
        self.contents_user1 = [[blank_char for col in range(num_cols)] for row in range(num_rows)]
        self.contents_user2 = [[blank_char for col in range(num_cols)] for row in range(num_rows)]
        self.blank_char = blank_char

    @property
    def num_rows(self) -> int:
        return len(self.contents_user1)

    @property
    def num_cols(self) -> int:
        return len(self.contents_user1[0])

    def __str__(self) -> str:
        """
          0 1 2
        0 X 0 *
        1 * * 0
        2 O O X
        :return:
        """
        sep = ' ' * max([len(str(self.num_rows)), len(str(self.num_cols))]) + '\n'
        rep = sep + sep.join((str(i) for i in range(self.num_cols)))
        for row_index, row in enumerate(self):
            rep += str(row_index) + sep + sep.join(row) + '\n'
        return rep

    def __iter__(self) -> Iterator[List[str]]:
        return iter(self.contents)

    def __getitem__(self, index: int) -> List[str]:
        return self.contents[index]



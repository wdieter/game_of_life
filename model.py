import copy
from typing import List


class Cell:
    __slots__ = ['val', 'x', 'y', 'neighbors']

    def __init__(self, val, x, y):
        self.val = val
        self.x = x
        self.y = y
        self.neighbors = None

    def __eq__(self, other):
        if other == self.val:
            return True

    def __add__(self, other):
        if isinstance(other, int):
            return int(self.val) + other
        return int(self.val) + int(other.val)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    @property
    def is_alive(self):
        return bool(self.val)


class Grid:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.dic = {(x, y): Cell(val=0, x=x, y=y) for x in range(width) for y in range(length)}
        self.view = [[self.dic[(x, y)] for x in range(width)] for y in range(length)]
        self._update_neighbors()

    def __str__(self):
        return '\n'.join([''.join(['_' if cell.val == 0 else '#' for cell in row]) for row in self.view])

    def set_alive(self, list_of_cell_xys):
        for cell_xy in list_of_cell_xys:
            self.dic[(cell_xy[0], cell_xy[1])].val = 1

    def play(self):
        print(self)
        self._update()

    def _update(self):
        old = copy.deepcopy(self.dic)
        for cell_xy, cell in old.items():
            neighbors_sum = self._get_neighbors_sum(cell.neighbors)
            if cell.is_alive:
                if neighbors_sum not in (2, 3):
                    self.dic[cell_xy].val = 0
            else:
                if neighbors_sum == 3:
                    self.dic[cell_xy].val = 1

    def _get_neighbors_sum(self, neighbors):
        return sum((self.dic[n] for n in neighbors))

    def _update_neighbors(self):
        """ after init, store a reference to a cell's neighbors in each cell.
        In this way we figure out who the neighbors are once, so next time we can simply iterate through them.
        """
        for cell_xy, cell in self.dic.items():
            cell.neighbors = self._get_neighbors_list(*cell_xy, self.width, self.length)

    @staticmethod
    def _get_neighbors_list(x, y, width, length):
        diffs = [-1, 0, 1]
        xs = [x + diff for diff in diffs if x + diff in range(width)]
        ys = [y + diff for diff in diffs if y + diff in range(length)]
        all_neighbors = tuple((nx, ny) for nx in xs for ny in ys if (nx, ny) != (x, y))
        return all_neighbors

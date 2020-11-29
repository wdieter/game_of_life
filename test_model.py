import pytest
import model


# Grid tests

def test_grid_init():
    """ grid can be initialized"""
    grid = model.Grid(5, 5)
    assert grid.dic[(0, 0)] == 0


def test_set_alive():
    """ we can set cells to be alive """
    grid = model.Grid(5, 5)
    grid.set_alive([[0, 0], [1, 0]])
    assert grid.dic[(0, 0)] == 1
    assert grid.dic[(1, 0)] == 1


neighbor_scenarios = [
    (2, 2, 5, 5, 8),  # middle of the grid with neighbors on all sides -> 8
    (0, 0, 5, 5, 3),  # top right corner -> 3
    (2, 0, 5, 5, 5),  # top middle of grid -> 5
    (2, 4, 5, 5, 5),  # bottom middle of grid -> 5
    (0, 2, 5, 5, 5),  # left middle of grid -> 5
    (4, 2, 5, 5, 5),  # right middle of grid -> 5
]


@pytest.mark.parametrize('x,y,width,length,expected', neighbor_scenarios)
def test_get_all_neighbors(x, y, width, length, expected):
    ns = model.Grid._get_neighbors_list(x, y, width, length)
    print(ns)
    assert len(ns) == expected


def test_update():
    """ test update works as expected, cells not alive after one round"""
    grid = model.Grid(5, 5)
    cells = [(0, 0), (1, 0)]
    grid.set_alive(cells)
    grid.play()
    for c in cells:
        cell = grid.dic[c]
        assert not cell.is_alive


# Grid Tests


# Cell tests

def test_cell_equality():
    cell = model.Cell(1, 0, 0)
    assert cell == 1


def test_cell_sum():
    cells = [model.Cell(1, 0, y) for y in range(2)]
    assert sum(cells) == 2

# Cell tests

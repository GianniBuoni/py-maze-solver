import random
from types import MethodType
from typing import Union, TYPE_CHECKING

if TYPE_CHECKING: from . import Maze

def _check_cell(self: "Maze", _, i, j) -> bool:
    if (
        i >= 0 and i < self._num_rows
        and j >= 0 and j < self._num_cols
        and self._cells[i][j].visited == False
    ):
        return True
    return False

def _get_rand_neighbor(
    _, i, j,
    check_func
) -> Union[tuple[str, tuple[int, int]], None]:

    can_visit = []
    directions: dict[str, tuple[int, int]] = {
        "up": (i - 1, j),
        "down": (i + 1, j),
        "left": (i, j - 1),
        "right": (i, j + 1)
    }

    for key in directions.keys():
        cell_idx = directions[key]
        if (
            check_func(key, *cell_idx)
        ):
            can_visit.append(key)

    if len(can_visit) == 0: return

    direction = random.choice(can_visit)
    next_idx = (directions[direction][0], directions[direction][1])
    return direction, next_idx

def _reset_cells_visited(self: "Maze"):
    for i in range(self._num_rows):
        for j in range(self._num_cols):
            self._cells[i][j].visited = False

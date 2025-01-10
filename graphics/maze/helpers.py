import random
from typing import Union, TYPE_CHECKING


if TYPE_CHECKING:
    from . import Maze
    from graphics.drawing import Cell

def _check_cell(self: "Maze", i, j) -> bool:
    if (
        i >= 0 and i < self._num_rows
        and j >= 0 and j < self._num_cols
        and self._cells[i][j].visited == False
    ):
        return True
    return False

def _check_move_cell(self: "Maze", direction, i, j) -> bool:
    if self._check_cell(i, j):
        cell: "Cell" = self._cells[i][j]
        match direction:
            case "up":
                return False if cell.has_bottom_wall else True
            case "down":
                return False if cell.has_top_wall else True
            case "left":
                return False if cell.has_right_wall else True
            case "right":
                return False if cell.has_left_wall else True
            case _: return False
    return False

def _get_rand_neighbor(
    self: "Maze", i, j,
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
        i2, j2 = directions[key]
        if self._check_cell(i2, j2):
            can_visit.append(key)

    if len(can_visit) == 0: return

    direction = random.choice(can_visit)
    next_idx = (directions[direction][0], directions[direction][1])
    return direction, next_idx

def _reset_cells_visited(self: "Maze"):
    for i in range(self._num_rows):
        for j in range(self._num_cols):
            self._cells[i][j].visited = False

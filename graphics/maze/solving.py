from typing import TYPE_CHECKING
if TYPE_CHECKING: from . import Maze

def solve(self: "Maze") -> bool:
    return self._solve_r(0,0)

def _solve_r(self: "Maze", i: int, j: int) -> bool:
    self._animate()
    self._cells[i][j].visited = True
    if (i == self._num_rows - 1) and (j == self._num_cols - 1): return True

    directions: dict[str, tuple[int, int]] = {
        "up": (i - 1, j),
        "down": (i + 1, j),
        "left": (i, j - 1),
        "right": (i, j + 1)
    }

    for key in directions.keys():
        i2, j2 = directions[key]
        if self._check_move_cell(key, i2, j2):
            self._cells[i][j].draw_move(self._cells[i2][j2])
            if self._solve_r(i2, j2):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i2][j2], True)
    return False

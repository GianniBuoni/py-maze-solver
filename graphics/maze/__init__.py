__all__ = ["Maze"]

import random
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from graphics.drawing import Cell
    from graphics.window import Window

class Maze():
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: float,
        cell_size_y: float,
        win: Union["Window", None] = None,
        seed: Union[int, None] = None
    ) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells: list[list["Cell"]] = []

        # events
        self._create_cells()
        self._break_entrance_and_exit()
        random.seed(seed)
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    from .break_walls import _break_entrance_and_exit, _break_walls_r
    from .drawing import _animate, _create_cells, _draw_cell
    from .helpers import _check_cell, _get_rand_neighbor, _reset_cells_visited

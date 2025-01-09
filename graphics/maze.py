from time import sleep
from typing import TYPE_CHECKING, Union
from graphics.drawing import Cell, Point

if TYPE_CHECKING:
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

    def _create_cells(self):
        for i in range(self._num_rows):
            row = []

            for j in range(self._num_cols):
                x = j * self._cell_size_x
                y = i * self._cell_size_y
                x1 = self._x1 + x
                x2 = x1 + self._cell_size_x
                y1 = self._y1 + y
                y2 = y1 + self._cell_size_y

                cell = Cell(Point(x1, y1), Point(x2, y2), self._win) # pyright: ignore
                row.append(cell)

            self._cells.append(row)

        if self._win is None: return
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_rows - 1][self._num_cols - 1].has_bottom_wall = False

        if self._win:
            self._draw_cell(0,0)
            self._draw_cell(self._num_rows -1, self._num_cols -1)

    def _animate(self):
        if self._win is None: return
        self._win.redraw()
        sleep(0.05)

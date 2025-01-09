import time
from graphics.drawing import Cell, Point
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import Maze

def _animate(self: "Maze"):
    if self._win is None: return
    self._win.redraw()
    time.sleep(0.05)

def _create_cells(self: "Maze"):
    for i in range(self._num_rows):
        row = []

        for j in range(self._num_cols):
            x = j * self._cell_size_x
            y = i * self._cell_size_y
            x1 = self._x1 + x
            x2 = x1 + self._cell_size_x
            y1 = self._y1 + y
            y2 = y1 + self._cell_size_y

            cell = Cell(Point(x1, y1), Point(x2, y2), self._win)
            row.append(cell)

        self._cells.append(row)

    if self._win is None: return
    for i in range(self._num_rows):
        for j in range(self._num_cols):
            self._draw_cell(i, j)

def _draw_cell(self: "Maze", i, j):
    self._cells[i][j].draw()
    self._animate()


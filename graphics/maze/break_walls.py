from typing import TYPE_CHECKING
if TYPE_CHECKING: from . import Maze

def _break_entrance_and_exit(self: "Maze"):
    self._cells[0][0].has_top_wall = False
    self._cells[self._num_rows - 1][self._num_cols - 1].has_bottom_wall = False

    if self._win:
        self._draw_cell(0,0)
        self._draw_cell(self._num_rows -1, self._num_cols -1)

def _break_walls_r(self: "Maze", i, j):
    cell = self._cells[i][j]
    cell.visited = True

    while True:
        if self._get_rand_neighbor(i, j) == None:
            self._draw_cell(i, j)
            return

        direction, next_idx = self._get_rand_neighbor(i, j) # pyright: ignore
        next_cell = self._cells[next_idx[0]][next_idx[1]]

        match direction:
            case "up":
                cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            case "down":
                cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            case "left":
                cell.has_left_wall = False
                next_cell.has_right_wall = False
            case "right":
                cell.has_right_wall = False
                next_cell.has_left_wall = False

        self._break_walls_r(*next_idx)

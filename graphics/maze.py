import random
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

    def _break_walls_r(self, i, j):
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

    def _get_rand_neighbor(self, i, j) -> Union[tuple[str, tuple[int, int]], None]:
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
                self._check_cell(*cell_idx)
                and self._cells[cell_idx[0]][cell_idx[1]].visited == False
            ):
                can_visit.append(key)

        if len(can_visit) == 0: return

        direction = random.choice(can_visit)
        next_idx = (directions[direction][0], directions[direction][1])
        return direction, next_idx

    def _check_cell(self, i, j) -> bool:
        if (i >= 0 and i < self._num_rows) and (j >= 0 and j < self._num_cols):
            return True
        return False

    def _animate(self):
        if self._win is None: return
        self._win.redraw()
        sleep(0.05)

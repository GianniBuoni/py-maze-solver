from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tkinter import Canvas
    from window import Window

class Point():
    def __init__(self, x, y) -> None:
        self.x, self.y = x, y

class Line():
    def __init__(self, point_1: "Point", point_2: "Point") -> None:
        self._x1 = point_1.x
        self._x2 = point_2.x
        self._y1 = point_1.y
        self._y2 = point_2.y

    def draw(self, canvas: "Canvas", fill_color: str):
        canvas.create_line(
            self._x1, self._y1,
            self._x2, self._y2,
            fill = fill_color,
            width = 2
        )

class Cell():
    def __init__(self, corner_1: "Point", corner_2: "Point", window: "Window" ) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = corner_1.x
        self._x2 = corner_2.x
        self._y1 = corner_1.y
        self._y2 = corner_2.y
        self._win = window

    def draw(self):
        # left wall
        top_point = Point(self._x1, self._y1)
        bottom_point = Point(self._x1, self._y2)
        self._win.draw_line(Line(top_point, bottom_point), "white" if self.has_left_wall else "black")

        # right wall
        top_point = Point(self._x2, self._y1)
        bottom_point = Point(self._x2, self._y2)
        self._win.draw_line(Line(top_point, bottom_point), "white" if self.has_right_wall else "black")

        # top wall
        left_point = Point(self._x1, self._y1)
        right_point = Point(self._x2, self._y1)
        self._win.draw_line(Line(left_point, right_point), "white" if self.has_top_wall else "black")

        # bottom wall
        left_point = Point(self._x1, self._y2)
        right_point = Point(self._x2, self._y2)
        self._win.draw_line(Line(left_point, right_point), "white" if self.has_bottom_wall else "black")

    def get_center(self) -> "Point":
        return Point(
            self._x1 + (self._x2 - self._x1) / 2,
            self._y1 + (self._y2 - self._y1) / 2
        )

    def draw_move(self, to_cell: "Cell", undo=False):
        fill_color = "gray" if undo else "red"
        self._win.draw_line(
            Line(self.get_center(), to_cell.get_center()),
            fill_color
        )

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tkinter import Canvas

class Point():
    def __init__(self, x, y) -> None:
        self.x, self.y = x, y

class Line():
    def __init__(self, point_1: "Point", point_2: "Point") -> None:
        self.__point_1 = point_1
        self.__point_2 = point_2

    def draw(self, canvas: "Canvas", fill_color: str):
        canvas.create_line(
            self.__point_1.x, self.__point_1.y,
            self.__point_2.x, self.__point_2.y,
            fill = fill_color,
            width = 2
        )


from tkinter import Tk, BOTH, Canvas
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from drawing import Line

class Window():
    def __init__(self, w, h) -> None:
        # root
        self.__root = Tk()
        self.__root.title("Maze Solver")

        # canvas
        self.__canvas = Canvas(
            self.__root, bg="black", width=w, height=h
        )
        self.__canvas.pack(fill=BOTH, expand=1)

        # running
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line: "Line", fill_color: str):
        line.draw(self.__canvas, fill_color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running: self.redraw()

    def close(self):
        self.__running = False

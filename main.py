from graphics import *
from graphics.drawing import Cell, Point

def main():
    win = window.Window(800, 600)
    cell_1 = Cell(Point(20,20), Point(500,200), win)
    cell_2 = Cell(Point(700, 500), Point(500,200), win)

    cell_1.draw()
    cell_2.draw()
    cell_2.draw_move(cell_1, True)

    win.wait_for_close()

if __name__ == "__main__":
    main()

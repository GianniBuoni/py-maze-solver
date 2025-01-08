from graphics import *
from graphics.drawing import Cell, Point

def main():
    win = window.Window(800, 600)
    Cell(Point(20,20), Point(500,200), win).draw()
    Cell(Point(1700, 500), Point(500,200), win).draw()
    win.wait_for_close()

if __name__ == "__main__":
    main()

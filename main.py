from graphics import *
from graphics.drawing import Line, Point

def main():
    test_line = Line(Point(0,20), Point(500,200))

    win = window.Window(800, 600)
    win.draw_line(test_line, "white")
    win.wait_for_close()

if __name__ == "__main__":
    main()

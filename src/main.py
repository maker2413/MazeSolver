from line import Line
from point import Point
from window import Window

def main():
    win = Window(800, 600)

    point1 = Point(10, 45)
    point2 = Point(100, 45)
    line1 = Line(point1, point2)

    win.draw_line(line=line1, fill_color="red")

    win.wait_for_close()

# This line ensures the main() function is only called when this file is run
# directly; it won't run if it's imported as a module.
if __name__ == "__main__":
    main()

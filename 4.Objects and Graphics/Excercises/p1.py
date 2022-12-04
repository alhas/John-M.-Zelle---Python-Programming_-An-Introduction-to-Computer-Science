from graphics import *


def main():
    win = GraphWin()

    shape = Rectangle(Point(1, 3), Point(4, 7))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)
        copy_shape = shape.clone()
        copy_shape.draw(win)

        if i == 8:
            Text(Point(1, 1), "One more click to exit").draw(win)

    win.close()


main()

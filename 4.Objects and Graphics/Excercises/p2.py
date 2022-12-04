from graphics import *

win = GraphWin("Archery Target")
yellow = Circle(Point(100, 100), 30)
blue = Circle(Point(100, 100), 25)
black = Circle(Point(100, 100), 20)
white = Circle(Point(100, 100), 15)

yellow.setOutline("red")
yellow.setFill("yellow")

blue.setOutline("blue")
black.setOutline("black")
white.setOutline("white")

colors = [yellow, blue, black, white]

for i in range(len(colors)):
    colors[i].setWidth(2)
    colors[i].draw(win)

win.getMouse()

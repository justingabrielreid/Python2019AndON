#!/usr/bin/env python3 

from graphics import *
#opening a graphics window
win = GraphWin("Shapes")
center = Point(100, 100)
circ = Circle(center, 30)
circ.setFill('red') 
circ.draw(win)
#place a textual label in the center of the circle
label = Text(center, "Red Circle")
label.draw(win)
#Draw a square using a Rectangle object
rect = Rectangle(Point(30,30), Point(70,70))
rect.draw(win)
#draw a line segment using a Line Object
line = Line(Point(20, 30), Point(80, 165))
line.draw(win)
### Draw an oval using an oval object 
oval = Oval(Point(20,150), Point(180,199))
oval.draw(win)


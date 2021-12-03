'''
CS 101 Lab
Program 12
Levi Lindskog is my name in Canvas, but I go by Levi Estabrook.
lhl8r5@umsystem.edu

PROBLEM:
Program must use the turtle module, classes and super classes
to draw and fill in boxes and circles.

ERROR HANDLING:
Error where boxes were being filled in with red instead of blue,
handled by including "turtle.fillcolor(self.fillcolor) beforehand.
'''

#ALGORITHM

import turtle


class Point(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()
    
    def draw_action(self):
        turtle.dot()


class Box(Point):
    def __init__(self, x1, y1, width, height, color):
        super().__init__(x1, y1, color)
        self.width = width
        self.height = height

    def draw_action(self):
        """Draws a box """
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)


class BoxFilled(Box):
    def __init__(self, x1, y1, width, height, color, fillcolor):
        super().__init__(x1,y1,width,height,color)
        self.fillcolor = fillcolor
    
    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()


class Circle(Point):
    def __init__(self,x1,y1,radius,color):
        super().__init__(x1,y1,color)
        self.radius = radius
    
    def draw_action(self):
        """Draws a circle"""
        turtle.circle(self.radius)


class CircleFilled(Circle):
    def __init__(self,x1,y1,radius,color,fillcolor):
        super().__init__(x1,y1,radius,color)
        self.fillcolor = fillcolor
    
    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()


if __name__ == "__main__":
    '''
    p = Point(-100, 100, "blue")
    p.draw()

    b = Box(100,110,50,40,"red")
    print(b.x,b.y,b.width,b.height,b.color)

    b = Box(-100,100,50,20,"blue")
    b.draw()

    b = BoxFilled(1, 2, 100, 200, "red", "blue")
    b.draw()

    c = CircleFilled(-1,-2,69,"black","green")
    c.draw()'''

    pnt = Point(100,100,"red")
    pnt.draw()
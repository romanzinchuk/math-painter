from random import randint

from canvas import Canvas
from figure import Square, Rectangle

canvas = Canvas(width=100, height=100, color=(255, 255, 255))

rectangle = Rectangle(x=randint(1, 29), y=randint(1, 29), width=randint(1, 30),
                      height= randint(1 , 30), color=(randint(0 , 255), randint(0 , 255),randint(0 , 255)))
rectangle.draw(canvas)
square = Square(x=randint(1, 29), y=randint(1, 29), side=randint(1, 30),
                color=(randint(0 , 255), randint(0 , 255),randint(0 , 255)))
square.draw(canvas)
canvas.make('canvas.png')


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from turtle import Turtle,Screen  # turtle.py scriptinden Turtle ve Screen classlarını getir
#from turtle import *

ninja=Turtle()

ninja.shape('turtle')
ninja.color('red')
ninja.shapesize(2, 2, 2)


# for i in range(4):
#     ninja.forward(100)
#     ninja.right(90)


i=1
while i<5:
    ninja.forward(100)
    ninja.right(90)
    i=i+1




# ninja.forward(100)
# ninja.right(90)
# ninja.forward(100)
# ninja.right(90)
# ninja.forward(100)

screen=Screen()
screen.exitonclick()



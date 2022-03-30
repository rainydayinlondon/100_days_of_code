# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Draw a Dashed Line


#from turtle import Turtle,Screen


from turtle import Turtle


tur = Turtle()


def drawdot(x):
    for i in range(x):
        tur.dot("blue")
       # turtle.dot(20, "blue");
        tur.forward(x)


tur.penup()
drawdot(10)

#tur.hideturtle()






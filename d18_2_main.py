import random
import turtle
import random

ninja = turtle.Turtle()

renkler=["pink","purple","blue","red","black","green","yellow"]
def draw_shape(num_side):
    for i in range(num_side):
        angle=360/num_side
        ninja.forward(100)
        ninja.right(angle)


for shape_side_n in range(3,11):
    ninja.color(random.choice(renkler))
    draw_shape(shape_side_n)









# ------------
# num_side=10
# for i in range(num_side):
#     angle=360/num_side
#     t.forward(100)
#     t.right(ange)
#
#
# -----------
# for i in range(5):
#     t.forward(100)  # Assuming the side of a pentagon is 100 units
#     t.right(72)  # Turning the turtle by 72 degree
#
# t = turtle.Turtle()
# for i in range(6):
#     t.forward(100)  # Assuming the side of a pentagon is 100 units
#     t.right(60)  # Turning the turtle by 72 degree
#
#
# for i in range(3):
#     t.forward(100)  # Assuming the side of a pentagon is 100 units
#     t.right(120)  # Turning the turtle by 72 degree



# ----------------------------------------
#
# numberOfSides = int(input('Enter the number of sides of a polygon: '))
# lengthOfSide = 100
# exteriorAngle = 360/numberOfSides
# for i in range(numberOfSides):
#    t.forward(lengthOfSide)
#    t.right(exteriorAngle)
#
#
#
# -----------------------------------



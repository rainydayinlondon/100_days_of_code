from turtle import Screen,Turtle



START_POINT=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANT=20

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]


    def create_snake(self):
        for position in START_POINT:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def snake_move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANT)


    def up(self):
        self.head.setheading(90)
       # self.head.forward(100)


    def down(self):
        self.head.setheading(270)
       # self.head.forward(100)


    def left(self):
        self.head.setheading(180)
       # self.head.forward(100)


    def right(self):
        self.head.setheading(0)
        #self.head.forward(100)


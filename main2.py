import turtle
from turtle import Screen,Turtle
from snake import Snake
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Heyyy Feyzaa'nın Yılan Oyununa Hosgeldin!")
screen.tracer(0)



snake_new=Snake()

screen.listen()
screen.onkey(snake_new.up,"Up")
screen.onkey(snake_new.down,"Down")
screen.onkey(snake_new.left,"Left")
screen.onkey(snake_new.right,"Right")






game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake_new.snake_move()








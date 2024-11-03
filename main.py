from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
#setting up snake body
screen =Screen()

screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)
screen.setup(width=600,height=600)
cordinates=[(0,0),(-20,0),(-40,0)]
segments=[]

snake =Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

#getting the snake to move
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detect collision with food
    if snake.segments[0].distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
#detect collison with wall
    if snake.segments[0].xcor() >280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() >280 or snake.segments[0].ycor() <-280:
        scoreboard.game_over()
        game_is_on = False




#detect collision with tail
#using slicing
for segment in snake.segments[1:]:
    if snake.segments[0].distance(segment) < 10:
        game_is_on = False
        scoreboard.game_over()

#if head collides with any segment in the tail
#trigger game over
#or

"""for segment in snake.segments:
    if segment == snake.segments[0]:
        pass
    if snake.segments[0].distance(segment)<10:
        game_is_on=False
        scoreboard.game_over()"""










screen.exitonclick()
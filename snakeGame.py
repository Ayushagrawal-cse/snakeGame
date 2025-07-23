from turtle import Screen
from snake import Snake
from food import Food
from scoreBoard import Scoreboard
import time



screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game ")
screen.tracer(0)

# staring_position=[(0,0),(-20,0),(-40,0)]
segment=[]

snake=Snake()
food=Food()
score=Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True

while game_is_on:
    screen.update()

    time.sleep(0.2)
    snake.move()
# detect collision
    if snake.segment[0].distance(food)< 15:
        food.refresh()
        snake.extend()
        score.increase_score()

#detect collision with wall
    if snake.segment[0].xcor()>290 or snake.segment[0].xcor()<-290 or snake.segment[0].ycor()>290 or snake.segment[0].ycor()<-290:
        game_is_on=False
        score.game_over()


#detect collision with tail
    for segment in snake.segment:
        if segment ==snake.segment[0]:
            pass
        elif snake.segment[0].distance(segment)<10:
            game_is_on=False
            score.reset()
            score.game_over()





screen.exitonclick()
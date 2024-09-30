import turtle
from turtle import Turtle,Screen
import random
import time
from turtledemo.penrose import start

from PIL.ImageChops import screen

my_screen = Screen()

player_dress_color = ['yellow','orange','red','black','blue']
positions = [(-300,-200),(-300,-100),(-300,0),(-300,100),(-300,200)]
finish_positions = []

name_of_game = Turtle()
name_of_game.penup()
name_of_game.hideturtle()
name_of_game.goto(0,300)
name_of_game.write("TURTLE GAME")

for i in range(-300,320,20):
    section = (300,i)
    finish_positions.append(section)

turtle_players = []
my_screen.tracer(0)

#creating individual turtles
for i in range(0,5):
    turtle_player = Turtle('turtle')
    turtle_player.penup()
    turtle_player.color(player_dress_color[i])
    turtle_player.goto(positions[i])
    turtle_players.append(turtle_player)

#creating finish line
for i in finish_positions:
    finish_line = Turtle('square')
    finish_line.penup()
    finish_line.color('black')
    finish_line.goto(i)


game_is_on = True
player_guess = input('Which turtle color wins?')

#game progress
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    for i in turtle_players:
        if i.xcor()>300:
            print(f"{i.pencolor()} is the winner")
            if player_guess == i.pencolor():
                print("you won")
            else:
                print("you lost")
            quit()
        i.forward(random.randint(0,10))

my_screen.exitonclick()
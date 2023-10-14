### Import Types of Library 
### Add Random Python Module.
### The Random module will be used to represent food and display random food location.

import turtle
import random


### Dimensions
 
w = 500
h = 500
food_size = 10
delay = 100
 
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}
 


### Function will be used to position food 

def reset():
    global snake, snake_dir, food_position, pen
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snake_dir = "up"
    food_position = get_random_food_position()
    food.goto(food_position)
    move_snake()

### Function will be used to determine snakes position

def move_snake():
    global snake_dir
 
    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_dir][0]
    new_head[1] = snake[-1][1] + offsets[snake_dir][1]
 
### if/else statement will be used to determind if snake take food object +/= 
### this creates a snake momevent effect. 

    if new_head in snake[:-1]:
        reset()
    else:
        snake.append(new_head)
 
     
        if not food_collision():
            snake.pop(0)
 
 
        if snake[-1][0] > w / 2:
            snake[-1][0] -= w
        elif snake[-1][0] < - w / 2:
            snake[-1][0] += w
        elif snake[-1][1] > h / 2:
            snake[-1][1] -= h
        elif snake[-1][1] < -h / 2:
            snake[-1][1] += h
 
 
        pen.clearstamps()
 
         
        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()
 
         
        screen.update()
 
        turtle.ontimer(move_snake, delay)
 

### If snake eats food position food a at random 

def food_collision():
    global food_position
    if get_distance(snake[-1], food_position) < 20:
        food_position = get_random_food_position()
        food.goto(food_position)
        return True
    return False
 
def get_random_food_position():
    x = random.randint(- w / 2 + food_size, w / 2 - food_size)
    y = random.randint(- h / 2 + food_size, h / 2 - food_size)
    return (x, y)

### snake direction

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance
def go_up():
    global snake_dir
    if snake_dir != "down":
        snake_dir = "up"
 
def go_right():
    global snake_dir
    if snake_dir != "left":
        snake_dir = "right"
 
def go_down():
    global snake_dir
    if snake_dir!= "up":
        snake_dir = "down"
 
def go_left():
    global snake_dir
    if snake_dir != "right":
        snake_dir = "left"


### Turtle Library will be used to display windown,
### window size, color and food size can be edited here. 
 
screen = turtle.Screen()
screen.setup(w, h)
screen.title("Snake")
screen.bgcolor("white")
screen.setup(500, 500)
screen.tracer(0)
 
 
pen = turtle.Turtle("square")
pen.penup()
 
 
food = turtle.Turtle()
food.shape("square")
food.color("red")
food.shapesize(food_size / 20)
food.penup()
 
 
### up,right,down,left keys will be used to position snake  


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
 
 
reset()
turtle.done()
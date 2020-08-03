import time
import turtle 
import random

BREAK_FLAG = False #for snake eating itself

# Draw window 
screen = turtle.Screen()
screen.title("Snake GAME NOKIA")
screen.bgcolor("lightgreen")
screen.setup(600,600)
screen.tracer(0) #for turning off animation

#Draw border
border = turtle.Turtle()
border.hideturtle()
border.penup()
border.goto(-300,300)#left up corner
border.pendown()
border.goto(300,300)
border.goto(300,-300)
border.goto(-300,-300) 
border.goto(-300,300)

#draw 3 pieced snake wih black head
snake = []
for i in range(3):
	snake_piece = turtle.Turtle()
	snake_piece.shape("square")
	snake_piece.penup()
	if i>0:
		snake_piece.color("gray")
	snake.append(snake_piece)

#draw food for snake
food = turtle.Turtle()
food.shape("circle")
food.penup()
food.goto(random.randrange(-300,300,20), random.randrange(-300,300,20))

#snake control
#pause control
PAUSE = 0
T = 0.1
def p():
	PAUSE=1
def u():
	PAUSE=0

screen.listen()

screen.onkeypress(lambda: snake[0].setheading(90), "Up")
screen.onkeypress(lambda: snake[0].setheading(270), "Down")
screen.onkeypress(lambda: snake[0].setheading(180), "Left")
screen.onkeypress(lambda: snake[0].setheading(0), "Right")
screen.onkeypress(p, "w")
screen.onkeypress(u, "s")



#Game logic
while True:
	#creating a new piece for snake
	#if snake eats food
	if snake[0].distance(food)<10:
		food.goto(random.randrange(-300,300,20),random.randrange(-300,300,20))
		snake_piece = turtle.Turtle()
		snake_piece.shape("square")
		snake_piece.color("gray")
		snake_piece.penup()
		snake.append(snake_piece)

	#snake body movement
	for i in range(len(snake)-1, 0, -1):
		x = snake[i-1].xcor()
		y = snake[i-1].ycor()
		snake[i].goto(x,y)

	#snake head movement
	snake[0].forward(20)

	#render
	screen.update()

	#snake collision with border
	x_cor = snake[0].xcor()
	y_cor = snake[0].ycor()
	if x_cor > 300 or x_cor < -300:
		screen.bgcolor("red")
		break
	if y_cor > 300 or y_cor < -300:
		screen.bgcolor("red")
		break 

	#snake collision with itself
	for i in snake[1:]:
		i = i.position()
		if snake[0].distance(i) < 10:
			screen.bgcolor("red")
			BREAK_FLAG = True
	if BREAK_FLAG:
		screen.bgcolor("red")
		break
	
	if PAUSE == 1:
		T = 2000
	elif PAUSE == 0:
		T = 0.1

	time.sleep(T)

screen.mainloop()
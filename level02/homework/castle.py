from turtle import *


#walls

width(7)
speed(10)
color("black")
forward(278)
left(90)
forward(200)
left(45)
forward(50)
left(90)
forward(50)
right(45)
forward(40)
right(90)
forward(100)
left(45)
forward(40)
left(90)
forward(40)
left(45)
forward(100)
right(90)
forward(40)
right(45)
forward(50)
left(90)
forward(50)
left(45)
forward(200)






#door
penup()
goto(115, 0)
pendown()

left(180)
forward(50)
right(90)
forward(40)
right(90)
forward(50)


#windows
penup()
goto(200, 150)
pendown()

forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

penup()
goto(70, 150)
pendown()


forward(45)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

exitonclick()
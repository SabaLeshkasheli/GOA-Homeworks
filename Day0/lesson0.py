from turtle import *

#we want to paint a house

#step 1 draw a square

# Walls 

width(7)
speed(10)
color("red")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#Door

forward(70)
left(90)
color("blue")
begin_fill()
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
#Roof

penup()
goto(200, 200)
pendown()

color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#Windows
#Left Window
penup()
goto(10, 60)
pendown()

color("purple")
right(150)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)

penup()
goto(30, 60)
pendown()

right(90)
forward(40)

penup()
goto(15, 80)
pendown()

right(90)
forward(35)
#Right window

penup()
goto(190, 60)
pendown()

color("green")
left(90)
forward(40) 
left(90)
forward(40) 
left(90)
forward(40) 
left(90)
forward(40) 

penup()
goto(170, 60)
pendown()

left(90)
forward(40)

penup()
goto(190, 80)
pendown()

left(90)
forward(35)




exitonclick()
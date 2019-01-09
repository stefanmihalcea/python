import turtle
from time import sleep

dist= 100
nr = 5
t = []

for i in range(nr):
  t.append(turtle.Turtle())

for i in range(nr):
  t[i].penup()
  t[i].hideturtle()
  t[i].speed(10)
  t[i].left(i*360/nr)
  t[i].forward(dist)

g = []

for i in range (nr):
  g.append(turtle.Turtle())

for i in range (nr):
  g[i].penup()
  g[i].hideturtle()
  g[i].speed(10)
  g[i].left(i*360/nr + 360/nr/2)
  g[i].forward(dist*2)

j= turtle.Turtle()
j.speed(10)
j.penup()
j.hideturtle()
j.setposition(t[0].position())
j.pendown()
for i in range (nr):
  j.goto(t[i].position())
  j.goto(g[i].position())

j.goto(t[0].position())

sleep(10)

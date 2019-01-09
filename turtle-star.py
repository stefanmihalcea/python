import turtle

dist= 100
nr = 13
t = []
g = []

for i in range(nr):
  t.append(turtle.Turtle())

for i in range(nr):
  t[i].hideturtle()
  t[i].penup()
  t[i].speed(100)
  t[i].left(i*360/nr)
  t[i].forward(dist)


for i in range (nr):
  g.append(turtle.Turtle())

for i in range (nr):
  g[i].hideturtle()
  g[i].penup()
  g[i].speed(100)
  g[i].left(i*360/nr + 360/nr/2)
  g[i].forward(dist*2)

j= turtle.Turtle()
j.hideturtle()
j.speed(10)
j.penup()

j.setposition(t[0])
j.pendown()
for i in range (nr):
  j.goto(t[i])
  j.goto(g[i])

j.goto(t[0])

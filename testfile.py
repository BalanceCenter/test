# 海龟做图，画一条蟒蛇
import turtle

turtle.setup(1000,600,200,200)
turtle.penup()
turtle.bk(300)
turtle.pendown()
turtle.pensize(50)
turtle.pencolor(0.64,0.35,0.28)
turtle.seth(90)
a = 0
b = 0
for i in range(3):
    turtle.circle(30+a+b,180)
    a += 20
    b += 10
    if i == 2:
        turtle.circle(30 + a + b, 100)

turtle.fd(20)
for i in range(2):
    turtle.circle(90, 80)
    turtle.circle(-90, 80)

turtle.circle(-90, 90)

for i in range(2):
    turtle.circle(90, 70)
    turtle.circle(-90, 70)
turtle.circle(90, 70/2)
turtle.fd(10)
turtle.circle(-30,180)
turtle.fd(80)
turtle.done()

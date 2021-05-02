import turtle
import time

def triangle(x1,y1,x2,y2,x3,y3,color):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x1,y1)

    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(x2,y2)
    turtle.goto(x3,y3)
    turtle.goto(x1,y1)
    turtle.end_fill()

    time.sleep(3)

def main():
    triangle(0,0,0,-200,300,300,'green')

main()

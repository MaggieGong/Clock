import turtle
import time
import keyboard
import os

turtle1 = turtle.Turtle()

def draw_gap():
    turtle1.penup()
    turtle1.fd(10)

def draw_line(draw):
    draw_gap()
    turtle1.pendown() if draw else turtle1.penup()
    turtle1.fd(100)
    draw_gap()
    turtle1.right(90)

def drawing_date(n):
    #goes right and turns right
    draw_line(True) if n in [8, 2, 3, 4, 5, 6, 9] else draw_line(False)
    #goes down and turns right
    draw_line(True) if n in [8, 0, 1, 3, 4, 5, 6, 7, 9] else draw_line(False)
    #goes left and turns right
    draw_line(True) if n in [8, 0, 2, 3, 5, 6, 9] else draw_line(False)
    #goes up and continues
    draw_line(True) if n in [8, 0, 2, 6] else draw_line(False)
    turtle1.left(90)
    #goes up and turns right
    draw_line(True) if n in [8, 0, 4, 5, 6, 9] else draw_line(False)
    #goes right and turns right
    draw_line(True) if n in [8, 0, 2, 3, 6, 7, 9, 5] else draw_line(False)
    #goes down and stops
    draw_line(True) if n in [8, 0, 1, 2, 3, 4, 7, 9] else draw_line(False)
    turtle1.left(180)
    turtle1.penup()
    turtle1.fd(40)

def draw(date):
    turtle1.pencolor("black")
    for n in date:
        if n == "h":
            turtle1.write(":", font=(10))
            turtle1.fd(40)
        elif n == "m":
            turtle1.write(":", font=(10))
            turtle1.fd(40)
        elif n == "s":
            turtle1.write(" ")
            turtle1.pencolor("black")
        else:
            drawing_date(eval(n))

def main():
    while True:
        turtle1.clear()
        turtle.setup(1920, 1080, 0, 0)
        here = os.path.dirname(os.path.abspath(__file__))
        background = os.path.join(here, "IMG_7402(20200915-010858).gif")
        turtle.bgpic(background)
        turtle1.speed(100)
        turtle1.penup()
        turtle1.goto(0, 0)
        turtle1.fd(-500)
        turtle1.pensize(10)
        local_time = time.strftime("%Ih%Mm%Ss", time.localtime()) if keyboard.is_pressed("Return") else time.strftime("%Hh%Mm%Ss", time.localtime())
        turtle1.getscreen().tracer(30, 0)
        draw(local_time)
        time.sleep(1)
        turtle1.hideturtle()

main()
        
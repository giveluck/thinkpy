import turtle
import math

bob = turtle.Turtle()

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
def polygon(t, n, length):
    angle = 360.0/n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def petal(t,r,angle):
    for i in range(2):
        arc(t,r,angle)
        t.lt(180-angle)
def flower(t,r,angle,leaf):
    t.speed(0)
    f_leaf = 360.0/leaf
    for i in range(leaf):
        petal(t,r,angle)
        t.lt(f_leaf)

flower(bob,100,108,5)

turtle.mainloop()
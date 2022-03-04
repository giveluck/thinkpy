import turtle
import math

bob = turtle.Turtle()

def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t,r):
    rad = r*2 * math.pi
    polygon(t,rad/360,360)

def arc(t, r, angle):
    radius = r * 2 * math.pi / 360

    for i in range(angle):
        t.fd(radius)
        t.lt(1)

arc(bob, 100, 180)




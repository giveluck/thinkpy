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

def tri(t,length,ract):
    t_angle = (180-360/ract)/2
    t_l = length/(math.sin(math.pi/ract)*2)
    t.fd(t_l)
    t.lt(180-t_angle)
    t.fd(length)
    t.lt(180-t_angle)
    t.fd(t_l)
    t.lt(180)

def pie(t,length,ract):
    for i in range(ract):
        tri(t,length,ract)




pie(bob,100,8)
turtle.mainloop()

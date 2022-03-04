import turtle

bob = turtle.Turtle()

def check_ferma(a, b, n,c):
    if a^n+b^n== c^n:
        print('역시 맞았어')
    else:
        print('페르마는 틀렸어')

def draw(t,length,n):
    if n==0:
        return
    angle =50
    t.fd(length*n)
    t.lt(angle)
    draw(t,length,n-1)
    t.rt(2*angle)
    draw(t,length,n-1)
    t.lt(angle)
    t.bs(length*n)

draw(bob,20,5)
turtle.mainloop()
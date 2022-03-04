#6-1
def b(z):
    prod = a(z,z)
    print(z,prod)
    return prod

def a(x,y):
    x = x+1
    return x* y

def c(x,y,z):
    total = x+y+z
    square = b(total)**2
    return square

#6-2
def ack(m,n):
    if isinstance(m, float):
        print('first number can input number')
        return None
    elif isinstance(n,float):
        print('scond number can input number')
        return None
    elif n <0:
        print('second number can input positive numbers')
    elif m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))
    else:
        print('뭔가가 잘못됐다 ')

print(ack(3,4))





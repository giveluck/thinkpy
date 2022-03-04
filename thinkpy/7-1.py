import math

def mysqrt(a):
    x=a/2
    while True:
        if a==1:
            return  1
            break
        y= (x+a/x)/2
        if y==x:
            return  y
            break
        x=y


def test_square_root():
    print('a',end='  ')
    print('mysqrt(a)',end='   ')
    print('math.sqrt(a)',end='   ')
    print('diff')
    print('-',end='  ')
    print('---------',end='   ')
    print('------------',end='   ')
    print('----')
    for i in range(1,10):
        print(i,end='  ')
        print('{:.7f}'.format(mysqrt(i)),end='   ')
        print('{:.10f}'.format(math.sqrt(i)),end='   ')
        print(mysqrt(i)-math.sqrt(i))



test_square_root()
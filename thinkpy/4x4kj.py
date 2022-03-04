def do_twice(f):
    f()
    f()

def do_four(f): #4함수 4번 실행
    do_twice(f)
    do_twice(f)

def f1(): #머리/층
    print('+', end=' ')
    print('-', '-', '-', '-', '+', end=' ')
    print('-', '-', '-', '-', '+', end=' ')
    print('-', '-', '-', '-', '+', end=' ')
    print('-', '-', '-', '-', end=' ')
    print('+')

def col():  #기둥
    print('|', end=' ')
    print(' ', ' ', ' ', ' ', '|', end=' ')
    print(' ', ' ', ' ', ' ', '|', end=' ')
    print(' ', ' ', ' ', ' ', '|', end=' ')
    print(' ', ' ', ' ', ' ', end=' ')
    print('|')

def kj4(): #4x4격자
    f1()
    do_four(col)
    f1()
    do_four(col)
    f1()
    do_four(col)
    f1()
    do_four(col)
    f1()
kj4()
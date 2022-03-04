import math

def eval_loop():
    while True:
        i = input('입력>')
        if i == 'done':
            break
        k = eval(i)
        print(k)

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result


def estimate_pi():
    k = 0
    total=0
    a= 2 * math.sqrt(2)/9801
    while True:
        b =factorial(4*k)*(1103+26390*k)
        c= factorial(k)**4 * 396**(4*k)
        result = a*b/c
        total += result
        if abs(result) < 1e-20:
            break
        k+=1
    return 1/total

print(estimate_pi())
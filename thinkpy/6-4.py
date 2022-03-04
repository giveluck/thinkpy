def is_power(a,b):
    if a%b==0:
        if b==a/b:
            print('power')
            return True
        return is_power(a/b,b)

is_power(1024,2)

def gcd(a,b):
    if a ==0:
        return b
    if b==0:
        return a
    if a >b:
        r = a%b
        return gcd(r,b)
    elif b>a:
        r= b%a
        return gcd(a,r)
    elif a==b:
        return a
    else:
        print('뭔가 잘못됐다')
        return None
x = gcd(1024,36)
print(x)

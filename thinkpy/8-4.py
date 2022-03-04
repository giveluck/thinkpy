def any_lowercase1(s): #s문자가 하나라도 소문자면 트루
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s): #다 트루나옴 잘못됨
    for c in s:
        if 'c'.islower():
            return True
        else:
            return False

def any_lowercas3(s): #s문자가 하나라도 소문자면 트루
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s): #얜무냐??????
    flag = False
    for c in s:
        flag = flag or c.islower
    return flag

def any_lowercase5(s): #하나라도 대문자면 False
    for c in s:
        if not c.islower():
            return False
    return True


def e9_1():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if len(word) >=20:
            print(word)

def has_no_e(word):
        if 'e'in word:
            return False
        return True
def e9_2():
    k = ""
    cnt = 0
    no = 0
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        cnt +=1
        if has_no_e(word) == True:
            k +=word
            k +='\n'
            no += 1
    re = str(no/cnt*100)
    k += re+'%'
    return k

def avoids(word,avoid):
    if avoid in word:
        return True
    return False

def e9_3(word,avoid):
    cnt =0
    for i in word:
        if i == avoid:
            cnt += 1
    if avoids(word,avoid):
        print('Change your word')
        print('THis word contains {0} alphabet'.format(cnt))

def uses_only(word,string):
    cnt = 0
    for i in string:
         for a in word:
             if a == i:
                 cnt +=1
    if cnt == 1:
        print('can use it')
        return True
    else:
        print('cant use it')


def uses_all(word,letter):
    for i in letter:
         for a in word:
            if a == i:
                return True

def e9_5(letter):
    cnt = 0
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if uses_all(word,letter) == True:
            cnt +=1
    print('Letters have {} vowels'.format(cnt))


fin = open('words.txt')
for line in fin:
    word = line.strip()
e9_5('aeiouy')

def rotate_word1(word):
    k = ''
    for a in 'abcdefghijklmnopqrstuvwxyz':
        for i in word:
            if ord(a) - ord(i) == 2:
                k += a
    return k

print(rotate_word1('apple'))

def rotate_letter(letter, n):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter
    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res

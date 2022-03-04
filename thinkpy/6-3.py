#6-3
def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if len(word)<=1:
        print('this word is palindrome')
        return True
    if first(word) != last(word):
        print('this word is not palindrome')
        return False
    return is_palindrome(middle(word))


is_palindrome('apple')
is_palindrome('odido')

def is_palindrome(word):
    if word == word[::-1]:
        print('this word is palindrome')
        return True
    else:
        print('this word is not palindrome')
        return False

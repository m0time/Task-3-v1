
def is_palindrome(word):

    cleanword = ''.join(c.lower() for c in word if c.isalnum())
    return cleanword == cleanword[::-1]


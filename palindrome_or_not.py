import re

def if_palindrome(rec):
    return rec[::-1]

def if_legal(rec):
    return re.findall("\D", rec)


palindrome = input('>>>')

if not int(len(if_legal(palindrome))) == int(len(palindrome)):
    raise Exception("Please, no digits")
else:
    if if_palindrome(palindrome) == palindrome:
        print("Word is a palindrome!")
    else:
        print("Word is not a palindrome!")
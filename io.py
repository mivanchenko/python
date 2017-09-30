def reverse(text):
    return text[::-1]

def normalize(text):
    norm = []
    for l in text:
        if str.isalpha(l):
            norm.append(l)
#    return str.lower(str.join('', norm))
    return ''.join(norm).lower()

def is_palindrome(text):
    return normalize(text) == reverse(normalize(text))

#something = input('Enter text: ')
something = "Rise to vote, sir."
if is_palindrome(something):
    print('Yes, it is a palindrome')
else:
    print('No, it is not a palindrome')

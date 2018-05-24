while True:
    try:
        a = input()
    except EOFError:
        break
    if a == a[::-1]:
        print('palindrome')
    else:
        print('not palindrome')
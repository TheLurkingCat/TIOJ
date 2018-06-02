while True:
    a = input()
    if a == 'END':
        break
    a = a.replace('+', '|')
    a = a.replace('*', '&')
    while '!' in a:
        a = a.replace('!0', '1')
        a = a.replace('!1', '0')
    print(eval(a))

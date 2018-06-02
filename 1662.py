while True:
    output = []
    try:
        a = input()
    except EOFError:
        break
    for word in a:
        if word.isupper():
            output.append(word.lower())
        elif word.islower():
            output.append(word.upper())
        else:
            output.append(' ')
    print(*output, sep='')

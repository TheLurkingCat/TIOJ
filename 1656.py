while True:
    try:
        a = int(input())
    except EOFError:
        break
    if a % 3:
        print('happy')
    else:
        if a % 9:
            print('sad')
        else:
            if a % 27:
                print('happy')
            else:
                print('sad')

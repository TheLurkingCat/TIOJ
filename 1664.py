week = {0:'Friday', 1:'Saturday', 2:'Sunday', 3:'Monday', 4:'Tuesday', 5:'Wednesday', 6:'Thursday'}
while True:
    try:
        a = int(input()) % 7
    except EOFError:
        break
    print(week[a])
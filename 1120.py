while True:
    output = '({},{})'
    try:
        t = int(input()) * 6 % 40
    except EOFError:
        break
    if 0 <= t <= 5:
        print(output.format(10+t, 5))
    elif 5 <= t <= 15:
        print(output.format(15, t))
    elif 15 <= t <= 25:
        print(output.format(30-t, 15))
    elif 25 <= t <= 35:
        print(output.format(5, 40-t))
    else:
        print(output.format(t-30, 5))

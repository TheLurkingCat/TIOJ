a, b = [int(x) for x in input().split()]
if a > b:
    print('Y' if (a/b).is_integer() else 'N')
else:
    print('Y' if (b/a).is_integer() else 'N')
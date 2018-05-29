from fractions import Fraction
a = int(input())
for _ in range(a):
    output = []
    x, y = [int(x) for x in input().split()]
    a, b = x, y
    opt = '+1/l{}{}r'
    ans = '{}{}'
    now = Fraction(x, y)
    while y:
        div, x = divmod(x, y)
        output.append(div)
        x, y = y, x
    k = len(output)
    for i in range(k-1):
        ans = ans.format(output[i], opt)
    ans = ans.format(output[-1], '')
    ans = ans.replace('l{}r'.format(output[-1]), str(output[-1]))
    ans = ans.replace('l', '{')
    ans = ans.replace('r', '}')
    print('{}/{} = {}'.format(a, b, ans))

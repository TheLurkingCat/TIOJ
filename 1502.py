"""
TLE
"""
from re import search
a = input()
b = input()
b = b.split('*')
s = ['(.*)'] * len(b)
s[-1] = ''
s[0] = ''
s = '{}'.join(s)
s = s.format(*b)
if search(s, a) is None:
    print('zzz...')
else:
    print('Asssssss!!!!!')

a = int(input())
for _ in range(a):
    left, right = input().split(' THEN ')
    left = left[3:]
    if 'and' in left:
        s1, s2 = left.split(' and ')
        left = 'not {} or not {}'.format(s1, s2)
    elif 'or' in left:
        s1, s2 = left.split(' or ')
        left = 'not {} and not {}'.format(s1, s2)
    else:
        left = 'not ' + left
    if 'and' in right:
        s1, s2 = right.split(' and ')
        right = 'not {} or not {}'.format(s1, s2)
    elif 'or' in right:
        s1, s2 = right.split(' or ')
        right = 'not {} and not {}'.format(s1, s2)
    else:
        right = 'not ' + right
    right = ''.join(right.split('not not '))
    left = ''.join(left.split('not not '))
    print('IF {} THEN {}'.format(right, left))

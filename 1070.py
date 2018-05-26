s = set(r"""~!@#$%^&*()_+|`-=\{}[]:";'<>?,./ """)
while True:
    up = True
    low = True
    digit = True
    special = True
    a = input()
    b = input()
    t = len(a)
    if a != b:
        print('Password settings are not consistent.')
    elif a == 'END':
        break
    else:
        if not 8 <= t <= 12:
            print('Password should contain 8 to 12 characters.')
            continue
        for char in a:
            if up and char.isupper():
                up = False
            if low and char.islower():
                low = False
            if digit and char.isdigit():
                digit = False
            if special and char in s:
                special = False
        if up:
            print('Password should contain at least one upper-case alphabetical character.')
            continue
        if low:
            print('Password should contain at least one lower-case alphabetical character.')
            continue
        if digit:
            print('Password should contain at least one number.')
            continue
        if special:
            print('Password should contain at least one special character.')
            continue
        if a == a[::-1]:
            print('Symmetric password is not allowed.')
            continue
        close = False
        for i in range(3, 7):
            j = 0
            k = 0
            while j < t:
                if k >= i:
                    k = 0
                if a[j] != a[k]:
                    break
                j += 1
                k += 1
            else:
                print('Circular password is not allowed.')
                break
        else:
            print('Password is valid.')
            
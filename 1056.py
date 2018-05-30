def check_matrix(mat):
    O_win = 0
    X_win = 0
    if mat[:3].count('O') == 3:
        O_win += 1
    if mat[:3].count('X') == 3:
        X_win += 1
    if mat[3:6].count('O') == 3:
        O_win += 1
    if mat[3:6].count('X') == 3:
        X_win += 1 
    if mat[6:].count('O') == 3:
        O_win += 1
    if mat[6:].count('X') == 3:
        X_win += 1
    if mat[::3].count('O') == 3:
        O_win += 1
    if mat[::3].count('X') == 3:
        X_win += 1
    if mat[1::3].count('O') == 3:
        O_win += 1
    if mat[1::3].count('X') == 3:
        X_win += 1
    if mat[2::3].count('O') == 3:
        O_win += 1
    if mat[2::3].count('X') == 3:
        X_win += 1
    if mat[::4].count('O') == 3:
        O_win += 1
    if mat[::4].count('X') == 3:
        X_win += 1
    if mat[2:8:2].count('O') == 3:
        O_win += 1
    if mat[2:8:2].count('X') == 3:
        X_win += 1
    return O_win, X_win
matrix = list(input()) + list(input()) + list(input())
for x in matrix:
    if not (x == 'O' or x == 'X' or x == '.'):
        print('IMPOSSIBLE')
        exit()
a = matrix.count('O')
b = matrix.count('X')
if a-b == 1:
    O, X = check_matrix(matrix)
    if (X == 0 and (O == 0 or O == 1 or O == 2)):
        print('POSSIBLE')
        exit()
elif a-b == 0:
    O, X = check_matrix(matrix)
    if (O == 0 and (X == 0 or X == 1 or X == 2)):
        print('POSSIBLE')
        exit()
print('IMPOSSIBLE')

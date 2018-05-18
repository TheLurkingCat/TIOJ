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
    if mat[2::3].count('O') == 3:
        O_win += 1
    if mat[2::3].count('X') == 3:
        X_win += 1
    if mat[3::3].count('O') == 3:
        O_win += 1
    if mat[3::3].count('X') == 3:
        X_win += 1
    if mat[::4].count('O') == 3:
        O_win += 1
    if mat[::4].count('X') == 3:
        X_win += 1
    if mat[3:8:2].count('O') == 3:
        O_win += 1
    if mat[3:8:3].count('X') == 3:
        X_win += 1
    return O_win, X_win
matrix = list(input()) + list(input()) + list(input())
a = matrix.count('O')
b = matrix.count('X')
if a-b == 1 or a-b == 0:
    O, X = check_matrix(matrix)
    if O + X > 1:
        print('IMPOSSIBLE')
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
print(matrix.count('.'))
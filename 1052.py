"""
這題五個等號後面有東西?
"""
a = int(input())
for _ in range(a):
    line = 0
    word = 0
    char = 0
    while True:
        try:
            temp = input()
        except EOFError:
            break
        if temp == '=====':
            break
        line += 1
        word += len(temp.split())
        char += len(temp)
    print(line, word, char)

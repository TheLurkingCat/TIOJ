from itertools import permutations
output = []
while True:
    try:
        a = input().strip()
    except EOFError:
        break
    output.append('')
    for x in permutations(a):
        output.append(''.join(x))
del output[0]
print(*output, sep='\n')
a = int(input())
b = int(input())
c = int(input())
output = []
if a + c == b + b:
    output.append('arithmetic')
a = a * c
k = b * b
if  a == k and a != 0 and k != 0:
    output.append('geometric')
if output:
    if len(output) == 2:
        print('both')
    else:
        print(output[0])
else:
    print('normal')
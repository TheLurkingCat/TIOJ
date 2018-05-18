a = input()
b = input()
x = min(len(a), len(b))
correct = []
for c in range(1, x+1):
    if b.endswith(a[:c]):
        correct.append(c)
if correct:
    print(max(correct))
else:
    print(0)
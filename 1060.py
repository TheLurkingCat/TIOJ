f_dict = {}
h_dict = {}
def f(x):
    if x in f_dict:
        return f_dict[x]
    k = h(x)
    if x > k:
        f_dict[x] = f(x-1) - k
        return f_dict[x]
    elif x < k:
        n = g(x)
        f_dict[x] = f(n) - n
        return f_dict[x]
    else:
        f_dict[x] = 1
        return 1
def h(x):
    if x in h_dict:
        return h_dict[x]
    if x < 2:
        h_dict[x] = -1
        return h_dict[x]
    h_dict[x] = 2 + h(x-1) - h(x-2)
    return h_dict[x]
def g(x):
    if x <= 2:
       return pow(x, 2) - 1
    return 2

for a in range(0, 600):
    f(300-a)
print(f_dict[int(input())])
"""
TLE
"""
a, b = [int(x) for x in input().split()]
mask = []
ip = []
mask_append = mask.append
ip_append = ip.append
for _ in range(a):
    c, d = input().split('/')
    d = int(d)
    mask_append(''.join([format(int(x), '08b') for x in c.split('.')])[:d])
for _ in range(b):
    c = ''.join([format(int(x), '08b') for x in input().split('.')])
    c_start = c.startswith
    for d in mask:
        if c_start(d):
            ip_append('TRUE')
            break
    else:
        ip_append('FALSE')
print(*ip, sep='\n')

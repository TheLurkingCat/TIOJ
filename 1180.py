ans = {0:1,1:1,2:2,3:6,4:24,5:120,6:720,7:5040,8:40320,9:362880,10:3628800,11:39916800,12:479001600,13:6227020800}
k = int(input())
for c in range(1, k+1):
    print('Case #{}:'.format(c))
    a = int(input())
    for x in range(a+1):
        print('TFCIS{}={}'.format(x, ans[x]))
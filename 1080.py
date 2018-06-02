def insertion_sort(lst):
    ans = 0
    if len(lst) == 1:
        return 0
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and temp < lst[j]:
            ans += 1
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp
    return ans


c = int(input())
while c:
    a = [int(x) for x in input().split()]
    print(insertion_sort(a))
    c = int(input())

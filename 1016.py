from collections import deque
while True:
    now = 0
    out = 0
    base = deque([0, 0, 0], maxlen=4)
    score = [0, 0]
    try:
        a = input()
    except EOFError:
        break
    for state in a:
        if state == 'K' or state == 'O':
            if out == 2:
                out = 0
                base = deque([0, 0, 0], maxlen=4)
                now = int(not now)
                continue
            else:
                out += 1
        elif state == 'S':
            base.appendleft(1)
            if len(base) == 4 and base.pop():
                score[now] += 1
        elif state == 'D':
            base.appendleft(1)
            if len(base) == 4 and base.pop():
                score[now] += 1
            base.appendleft(0)
            if len(base) == 4 and base.pop():
                score[now] += 1
        elif state == 'T':
            base.appendleft(1)
            if len(base) == 4 and base.pop():
                score[now] += 1
            base.appendleft(0)
            if len(base) == 4 and base.pop():
                score[now] += 1
            base.appendleft(0)
            if len(base) == 4 and base.pop():
                score[now] += 1
        elif state == 'H':
            score[now] += sum(base) + 1
            base = deque([0, 0, 0], maxlen=4)
        elif state == 'W':
            if base[0]:
                if base[1]:
                    if base[2]:
                        score[now] += 1
                    else:
                        base[2] = 1
                else:
                    base[1] = 1
            else:
                base[0] = 1
    print(*score)

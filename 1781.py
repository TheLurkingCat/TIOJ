from html.parser import HTMLParser
from collections import Counter, deque
from sys import stdin
accepted = deque([], maxlen=9)
failed = []
out = []
out_append = out.append
ac_append = accepted.append
failed_append = failed.append


class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        k = [bool(x) for x in accepted]
        data = data.strip()
        if data == 'Accepted':
            datas[accepted[-2]] += 1
        elif len(k) == 9 and k[0] and k[1] and k[2] and k[3] and not k[4] and not k[5] and k[6] and k[7] and k[8]:
            failed_append(accepted[1])
        data = data.replace('\n', '')
        ac_append(data)


parser = MyHTMLParser()
datas = Counter()
parser.feed(''.join(stdin))
t = None
for x, y in datas.most_common():
    if t is None:
        t = y
    elif t != y:
        break
    out_append(x)
out.sort()
try:
    print(out[0], t, sep=': ')
except IndexError:
    failed.sort()
    print('{}: 0'.format(failed[0]))

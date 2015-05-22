from datetime import date as d
from operator import mul as m

def valid(s):
    x = [3, 2, 7, 6, 5, 4, 3, 2]
    y = {'0': '20', '9' : '19'}
    t = -1

    try:
        d(int(y[s[9]]+ s[4:6]), int(s[2:4]), int(s[0:2]))
        t = (11 - (sum(map(m, x, [int(x) for x in list(s[:-2])])) % 11))

    finally:
        return t == int(s[8])

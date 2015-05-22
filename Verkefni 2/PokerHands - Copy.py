def rank_hand(h):
    s = [x for r, x in h]
    p = ['--23456789TJQKA'.index(x) for x, r in h]
    p.sort(reverse=True)

    f = len(set(s)) == 1
    z = max(p)-min(p) == 4 and len(set(p)) == 5

    def k(n, e=None):
        for r in p:
            if p.count(r) == n and r != e:
                return r              

    if z and f and max(p) == 14:
        return 9
    if z and f:
        return 8
    if k(4):
        return 7
    if k(3) and k(2):
        return 6
    if f:
        return 5
    if z:
        return 4
    if k(3):
        return 3
    if k(2) and k(2, k(2)):
        return 2
    if k(2):
        return 1
    return 0


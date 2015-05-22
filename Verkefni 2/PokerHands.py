def rank_hand(h):
    suits = [x for r, x in h]
    ranks = ['--23456789TJQKA'.index(x) for x, r in h]
    ranks.sort(reverse=True)

    f = len(set(suits)) == 1
    s = (max(ranks)-min(ranks)) == 4 and len(set(ranks)) == 5

    def k(n, e=None):
        for r in ranks:
            if ranks.count(r) == n and r != e:
                return r

    if s and f and max(ranks) == 14:
        return 9
    if s and f:
        return 8
    if k(4):
        return 7
    if k(3) and k(2):
        return 6
    if f:
        return 5
    if s:
        return 4
    if k(3):
        return 3
    if k(2) and k(2, k(2)): 
        return 2
    if k(2):
        return 1
    return 0



rank_hand([ '3D', '2H', '3C', 'QS', '8D' ]) # 1

rank_hand(['7H', '8C', '5D', '7S', '5C']) # 2

rank_hand([ 'KD', 'KH', 'KC', 'TS', 'TD' ]) # 6

rank_hand([ 'JD', 'KD', 'TD', 'QD', 'AD' ]) # 9

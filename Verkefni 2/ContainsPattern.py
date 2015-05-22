from itertools import combinations
def contains_pattern(p, a):
    c = list(combinations(p, len(a)))
    for x in c:
        f = [ sorted(x).index(y) for y in x ]
        if f == a: return True
        
    return False

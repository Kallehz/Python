from itertools import combinations
def contains_pattern(p, a):
    c = list(combinations(p, len(a)))
    for x in c:
        if list(sorted(x).index(y) for y in x) == a:
            return True
        
    return False

print(contains_pattern([4,0,2,1,3],[1,0]))
print(contains_pattern([4,0,2,1,3],[2,0,1]))
print(contains_pattern([0,1,2,3,4,5],[1,0]))

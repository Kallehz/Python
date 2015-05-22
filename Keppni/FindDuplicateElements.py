from collections import Counter as c
def duplicates(s): 
    return [x for x, y in c(s).items() if y > 1]

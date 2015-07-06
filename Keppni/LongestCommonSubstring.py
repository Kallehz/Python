import itertools

def longest_common_substring(words):
    sublis = []
    for x in words:
        length = len(x)
        sublis.append([x[i:j+1] for i in range(length) for j in range(i,length)])
          
    y = set(sublis[0])
    for x in sublis[1:]:
        y.intersection_update(x)
    if len(y) > 0:
        y = max(y, key=len)
        return (len(y))
    return 0;



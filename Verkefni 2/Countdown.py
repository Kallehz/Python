from itertools import permutations
import fileinput

def countdown(filename, string):
    w = []
    file = open(filename)
    for line in file:
        w.append(line.strip())

    p = []
    for x in range(3, len(string)+1):           
        p += list(''.join(p) for p in permutations(string, x))
        
    
    lis = list(set(p).intersection(w))
    lis.sort(key=str.lower)
    return(lis)

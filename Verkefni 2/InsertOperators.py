import itertools as it
def insert_operators(q, t):
    o = list(it.product(['+', '-', ''], repeat=len(q) - 1))
    for x in o:
        eq = list(it.zip_longest(q, x))
  
        s = ''
 
        for e in eq:
            s += str(e[0])
            if (e[1] != None):
                s += e[1]
 
        if (eval(s) == t):
            return s + '=' + str(t)
 
    return None





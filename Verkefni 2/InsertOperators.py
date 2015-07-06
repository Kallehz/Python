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
            print( s + '=' + str(t))
 
    return None

insert_operators([14,8,2,17,5,9],83)
# "14+82-17-5+9=83"
insert_operators([34,9,82,21,32],32850)
# "34982-2132=32850"
insert_operators([1,2,3],5)
# None





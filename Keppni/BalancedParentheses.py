def balanced(p):
    c = 0
    for x in p:
        if c < 0:
            break
        if x is '(':
            c += 1
        else:
            c -= 1
        
    return c is 0


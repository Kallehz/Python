def process_ls(s):
    l = [' '.join(x.split()) for x in s.splitlines()]
    l = [x.split(' ', 8) for x in l if x[0] != 'd']
    l = sorted(l, key=lambda x: x[8], reverse=True)
    l = sorted(l, key=lambda x: int(x[4]))
    n = []
    for x in l:
        n.insert(0, x[8])
           
    return n



